import math
import torch
import torch.nn as nn
import torchvision
from . import block as B
from . import spectral_norm as SN
from math import sqrt
from torch.nn.parameter import Parameter
from torch.nn import init
import torch.nn.functional as F
import scipy.io as sio
import numpy as np
####################
# Generator
####################


#############################RlcscNet###############################
class MySCN(nn.Module):
    def __init__(self):
        super(MySCN, self).__init__()
        self.W1 = nn.Conv2d(128, 256, 3, 1, 1, bias=False)
        self.S = nn.Conv2d(256, 256, 3, 1, 1, groups=1, bias=False)
        self.W2 = nn.Conv2d(256, 128, 3, 1, 1, bias=False)
        self.RW1 = CALayer(256,16)
        self.RW2 = CALayer(256,16)
        self.shlu = nn.ReLU(True)
        self.relu = nn.ReLU(True)
        
        self.T = Parameter(torch.Tensor(1))
        nn.init.constant(self.T,0)

    def forward(self, input):

        z = self.W1(input)   
        tmp = z
        for _ in range(25):
            
            x = self.RW2(self.shlu( self.RW1(tmp)[0] - self.T))[0]
            x = self.S(x)
            tmp = x + z

        c = self.RW2(self.shlu( self.RW1( x+z )[0] - self.T))[0]
        ####################  rain density estimation  ########################################
        #rde = self.RW1( x+z )[1].data[0,:,0,0].cpu().numpy().astype(np.float32)
        #print(np.mean(rde))
        #f = open('rde.txt','a')
        #f.write('{} \n'.format(np.mean(rde)))
        #f.close()
        #################################################################################################
        out = self.W2(c)
        out = self.relu(out)
        return out

class RlcscNet(nn.Module):
    def __init__(self):
        super(RlcscNet, self).__init__()
        self.scn = MySCN()
        self.input = nn.Conv2d(in_channels=3, out_channels=128, kernel_size=3, stride=1, padding=1, bias=False)
        self.advanced = nn.Conv2d(in_channels=128, out_channels=128, kernel_size=3, stride=1, padding=1, bias=False)
        self.output = nn.Conv2d(in_channels=128, out_channels=3, kernel_size=3, stride=1, padding=1, bias=False)
        self.relu = nn.ReLU(inplace=True)
    
        for m in self.modules():
            if isinstance(m, nn.Conv2d):
                #print(m)
                n = m.kernel_size[0] * m.kernel_size[1] * m.out_channels
                m.weight.data.normal_(0, sqrt(2. / n))
                #print(m.weight)


    def forward(self, x):
        residual = x
        out = self.relu(self.input(x))
        out = self.relu(self.advanced(out))
        out = self.scn(out)
        out = self.output(out)
        out = torch.add(out,residual)
        return out

############################  ms_rlcsc_net ###############################
class MSRlcscNet(nn.Module):
    def __init__(self):
        super(MSRlcscNet, self).__init__()
        self.scn = MS_MySCN()
        self.input = nn.Conv2d(in_channels=3, out_channels=48, kernel_size=3, stride=1, padding=1, bias=False)
        self.advanced = nn.Conv2d(in_channels=48, out_channels=48, kernel_size=3, stride=1, padding=1, bias=False)
        self.output = nn.Conv2d(in_channels=48, out_channels=3, kernel_size=3, stride=1, padding=1, bias=False)
        self.relu = nn.ReLU(inplace=True)
    
        for m in self.modules():
            if isinstance(m, nn.Conv2d):
                #print(m)
                n = m.kernel_size[0] * m.kernel_size[1] * m.out_channels
                m.weight.data.normal_(0, sqrt(2. / n))
                #print(m.weight)


    def forward(self, x):
        residual = x
        out = self.relu(self.input(x))
        out = self.relu(self.advanced(out)) 
        out = self.scn(out)
        out = self.output(out)
        out = torch.add(out,residual)
        return out

class MS_MySCN(nn.Module):
    def __init__(self):
        super(MS_MySCN,self).__init__()
        self.D1 = nn.Conv2d(96,48,kernel_size=3,stride=1,padding=1,bias=False)
        self.DT1= nn.Conv2d(48,96,kernel_size=3,stride=1,padding=1,bias=False) 
        self.D2 = nn.Conv2d(96,48,kernel_size=5,stride=1,padding=2,bias=False)
        self.DT2= nn.Conv2d(48,96,kernel_size=5,stride=1,padding=2,bias=False) 
        self.D3 = nn.Conv2d(96,48,kernel_size=7,stride=1,padding=3,bias=False)
        self.DT3= nn.Conv2d(48,96,kernel_size=7,stride=1,padding=3,bias=False)
        self.RW1_1 = CALayer(96,8)
        self.RW1_2 = CALayer(96,8)
        self.RW2_1 = CALayer(96,8)
        self.RW2_2 = CALayer(96,8)
        self.RW3_1 = CALayer(96,8)
        self.RW3_2 = CALayer(96,8)
        self.shlu = nn.ReLU()   
        self.relu = nn.ReLU()

        self.T1 = Parameter(torch.Tensor(26))
        nn.init.constant(self.T1,0)
        self.T2 = Parameter(torch.Tensor(26))
        nn.init.constant(self.T2,0)
        self.T3 = Parameter(torch.Tensor(26))
        nn.init.constant(self.T3,0)


    def forward(self,inp):

        z1_0 = self.RW1_2(self.shlu(self.RW1_1( self.DT1(inp)-self.T1[0] )[0]))[0]
        z2_0 = self.RW2_2(self.shlu(self.RW2_1( self.DT2(inp)-self.T2[0] )[0]))[0]
        z3_0 = self.RW3_2(self.shlu(self.RW3_1( self.DT3(inp)-self.T3[0] )[0]))[0]
        ssum = 0

        for i in range(25):
            tmp1 = self.D1(z1_0)
            tmp2 = self.D2(z2_0)
            tmp3 = self.D3(z3_0)
            z1_1 = self.RW1_2(self.shlu(self.RW1_1( z1_0 + self.DT1(inp-tmp1-tmp2-tmp3)-self.T1[i+1] )[0]))[0]
            z2_1 = self.RW2_2(self.shlu(self.RW2_1( z2_0 + self.DT2(inp-tmp1-tmp2-tmp3)-self.T2[i+1] )[0]))[0]
            z3_1 = self.RW3_2(self.shlu(self.RW3_1( z3_0 + self.DT3(inp-tmp1-tmp2-tmp3)-self.T3[i+1] )[0]))[0]

            z1_0 = z1_1
            z2_0 = z2_1
            z3_0 = z3_1

        c = self.D1(z1_1)+self.D2(z2_1)+self.D3(z3_1)
        out = self.relu(c)
        

        return out

######################  end ms_rlcsc_net ##############################


## channel attention layer for AC(act->conv)
class CALayer(nn.Module):
    def __init__(self,channel,reduction=16):
        super(CALayer,self).__init__()
        # global average pooling:feature(H*W*C)->point(1*1*C)
        self.ave_pool   = nn.AdaptiveAvgPool2d(1)
        self.conv_atten = nn.Sequential(
            nn.Conv2d(channel,channel//reduction,1,padding=0,bias=False),
            nn.ReLU(True),
            nn.Conv2d(channel//reduction,channel,1,padding=0,bias=False),
            nn.Sigmoid())


    def forward(self,inp):
        atte = self.ave_pool(inp)
        atte = self.conv_atten(atte)

        return inp*atte,atte

