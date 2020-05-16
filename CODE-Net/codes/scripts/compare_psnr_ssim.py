import cv2
import numpy as np
from skimage.measure import compare_psnr,compare_ssim
import glob

derain_folder = '/home/spl/anaconda2/envs/pth10-py36-cu10/PReNet-master/results/test1000/*'
gt_folder = '/home/spl/anaconda2/envs/pth10-py36-cu10/deraining_esrgan/datasets/Real_Rain_Streaks_Dataset_CVPR19_spanet/Testing/real_test_1000/real_test_1000/gt/*'

derain_list = sorted(glob.glob(derain_folder))
gt_list = sorted(glob.glob(gt_folder))

psnr=[]
ssim=[]

for i in range(len(gt_list)):

    im1 = cv2.imread(derain_list[i]).astype(np.float32) / 255.0 
    im2 = cv2.imread(gt_list[i]).astype(np.float32) / 255.0 

    psnr.append(compare_psnr(im1,im2))
    ssim.append(compare_ssim(im1,im2,multichannel=True))

print(np.mean(psnr),np.mean(ssim))
    