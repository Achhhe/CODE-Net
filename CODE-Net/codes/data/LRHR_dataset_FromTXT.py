import os.path
import random
import numpy as np
import cv2
import torch
import torch.utils.data as data
import data.util as util


class LRHRDataset_FromTXT(data.Dataset):
    '''
    Read LR and HR image pairs.
    If only HR image is provided, generate LR image on-the-fly.
    The pair is ensured by 'sorted' function, so please check the name convention.
    '''

    def __init__(self, txt_path,opt):
        super(LRHRDataset_FromTXT, self).__init__()
        ftxt = open(txt_path,'r')

        imgs = []
        for line in ftxt:
            imgs.append(line.rstrip())
        self.imgs = imgs
        self.opt=opt


    def __getitem__(self, index):
        HR_path, LR_path = None, None
        HR_size = self.opt['HR_size']
        scale = self.opt['scale']
        LR_path, HR_path = self.imgs[index].split()
        LR_path = '/home/spl/anaconda2/envs/pth10-py36-cu10/deraining_esrgan/datasets/Real_Rain_Streaks_Dataset_CVPR19_spanet/Training' + LR_path
        HR_path = '/home/spl/anaconda2/envs/pth10-py36-cu10/deraining_esrgan/datasets/Real_Rain_Streaks_Dataset_CVPR19_spanet/Training' + HR_path

        img_HR = util.read_img(None, HR_path)
        img_LR = util.read_img(None, LR_path)

        # modcrop in the validation / test phase

        if self.opt['color']:
            img_HR = util.channel_convert(img_HR.shape[2], self.opt['color'], [img_HR])[0]



        # if the image size is too small
        H, W, _ = img_HR.shape
        if H < HR_size or W < HR_size:
            img_HR = cv2.resize(
                np.copy(img_HR), (HR_size, HR_size), interpolation=cv2.INTER_LINEAR)
            # using matlab imresize
            img_LR = util.imresize_np(img_HR, 1 / scale, True)
            if img_LR.ndim == 2:
                img_LR = np.expand_dims(img_LR, axis=2)

        # ####################################
        H, W, C = img_LR.shape
        LR_size = HR_size // scale

        # randomly crop
        rnd_h = random.randint(0, max(0, H - LR_size))
        rnd_w = random.randint(0, max(0, W - LR_size))
        img_LR = img_LR[rnd_h:rnd_h + LR_size, rnd_w:rnd_w + LR_size, :]
        rnd_h_HR, rnd_w_HR = int(rnd_h * scale), int(rnd_w * scale)
        img_HR = img_HR[rnd_h_HR:rnd_h_HR + HR_size, rnd_w_HR:rnd_w_HR + HR_size, :]

        # augmentation - flip, rotate
        img_LR, img_HR = util.augment([img_LR, img_HR], self.opt['use_flip'], \
            self.opt['use_rot'])
        ##############################################

        # change color space if necessary
        if self.opt['color']:
            img_LR = util.channel_convert(C, self.opt['color'], [img_LR])[0] # TODO during val no definetion

        # BGR to RGB, HWC to CHW, numpy to tensor
        if img_HR.shape[2] == 3:
            img_HR = img_HR[:, :, [2, 1, 0]]
            img_LR = img_LR[:, :, [2, 1, 0]]
        img_HR = torch.from_numpy(np.ascontiguousarray(np.transpose(img_HR, (2, 0, 1)))).float()
        img_LR = torch.from_numpy(np.ascontiguousarray(np.transpose(img_LR, (2, 0, 1)))).float()

        return {'LR': img_LR, 'HR': img_HR, 'LR_path': LR_path, 'HR_path': HR_path}

    def __len__(self):
        return len(self.imgs)
