## Dependencies

* Python 3 (Recommend to use [Anaconda](https://www.anaconda.com/distribution/#linux))
* [Pytorch 1.0.1](https://pytorch.org/)
* NVIDIA GPU + [CUDA](https://developer.nvidia.com/cuda-downloads)
* Python packages: pip install opencv-python, visdom

## Dataset

We use 12000 and 1800 pairs of images from [DID-MDN](https://github.com/hezhangsprinter/DID-MDN) and [JORDER](http://www.icst.pku.edu.cn/struct/Projects/joint_rain_removal.html), and a high quality real rain dataset from [SPANet](https://stevewongv.github.io/derain-project.html) as training sets. For testing, three commonly synthetic datasets, [Rain1200](https://github.com/hezhangsprinter/DID-MDN), [Rain12](http://openaccess.thecvf.com/content_cvpr_2016/papers/Li_Rain_Streak_Removal_CVPR_2016_paper.pdf) and [Testing1000](https://stevewongv.github.io/derain-project.html) and some [real-world](https://pan.baidu.com/s/1crBm7pbjXfg3MiiCDbxWzA) (psw:nhra) images are utilized

## Clone

`git clone https://github.com/Achhhe/CODE-Net.git --depth==1`

## Train

1. Modify the configuration file  `options/train/train_sr.json`
2. Run command: `python train.py -opt options/train/train_sr.json`

*Note that: `using_spanet_dadaset = True` to use SPANet dataset for training*

## Testing

1. Modify the configuration file `options/test/test_sr.json` 
1. Run command: `python test.py -opt options/test/test_sr.json`

## Visualizer

We also add a visualizer module, for visualizing training process.

Run command: `python -m visdom.server`

*Note that: if the display screen shows no images, just blue, you can download the [static.zip](https://pan.baidu.com/s/1crBm7pbjXfg3MiiCDbxWzA) (psw:nhra) to replace the same file in `xxx/lib/python3.6/site-packages/visdom` or change the display port*

## Pretrained Models + Results

Avoid training or testing, you could download the pretrained models or deraining results on Rain1200/Rain12/Testing1000/RealImages  from  [BaiduNetdisk](https://pan.baidu.com/s/1crBm7pbjXfg3MiiCDbxWzA) (psw:nhra) directly.

## Acknowledgements

Code architecture borrows from [BasicSR](https://github.com/xinntao/BasicSR) and the visualizer is inspired by [pytorch-cyclegan](https://github.com/junyanz/pytorch-CycleGAN-and-pix2pix). Thanks for sharing!

