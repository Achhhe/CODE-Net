# Configurations
- Use **json** files to configure options.
- Convert the json file to python dict.
- Support `//` comments and use `null` for `None`.

## Table
Click for detailed explanations for each json file.

1. [train_sr.json](#train_sr_json)

## train_sr_json
```c++
{
  "name": "debug_001_RRDB_PSNR_x4_DIV2K" //  leading 'debug_' enters the 'debug' mode. Please remove it during formal training
  , "use_tb_logger": true // use tensorboard_logger, ref: `https://github.com/xinntao/BasicSR/tree/master/codes/utils`
  , "model":"sr" // model type, ref: `https://github.com/xinntao/BasicSR/blob/master/codes/models/__init__.py`
  , "scale": 1 // scale factor for SR
  , "gpu_ids": [0] // specify GPUs, actually it sets the `CUDA_VISIBLE_DEVICES`

  , "datasets": { // configure the training and validation datasets
    "train": { // training dataset configurations
      "name": "DIV2K" // dataset name
      , "mode": "LRHR" // dataset mode, ref: `https://github.com/xinntao/BasicSR/blob/master/codes/data/__init__.py`
      , "dataroot_HR": "/mnt/SSD/xtwang/BasicSR_datasets/DIV2K800/DIV2K800_sub.lmdb" // HR data root
      , "dataroot_LR": "/mnt/SSD/xtwang/BasicSR_datasets/DIV2K800/DIV2K800_sub_bicLRx4.lmdb" // LR data root
      , "subset_file": null // use a subset of an image folder
      , "use_shuffle": true // shuffle the dataset
      , "n_workers": 8 // number of data load workers
      , "batch_size": 16
      , "HR_size": 128 // 128 | 192, cropped HR patch size
      , "use_flip": true // whether use horizontal and vertical flips
      , "use_rot": true // whether use rotations: 90, 190, 270 degrees
    }
    , "val": { // validation dataset configurations
      "name": "val_set5"
      , "mode": "LRHR"
      , "dataroot_HR": "/mnt/SSD/xtwang/BasicSR_datasets/val_set5/Set5"
      , "dataroot_LR": "/mnt/SSD/xtwang/BasicSR_datasets/val_set5/Set5_bicLRx4"
    }
  }

  , "path": {
    "root": "/home/xtwang/Projects/BasicSR" // root path
    , "pretrain_model_G": null // path of the pretrained model
  }

  , "network_G": { // configurations for the network G
    "which_model_G": "rlcsc_net" // rlcsc_net | ms_rlcsc_net, network structures, ref: `./codes/models/networks.py`
    , "norm_type": null // null | "batch", norm type 
    , "mode": "CNA" // Convolution mode: CNA for Conv-Norm_Activation
    , "nf": 64 // number of features for each layer
    , "nb": 23 // number of blocks
    , "in_nc": 3 // input channels
    , "out_nc": 3 // output channels
    , "gc": 32 // grouwing channels, for Dense Block
    , "group": 1 // convolution group, for ResNeXt Block
  }

  , "train": { // training strategies
    "lr_G": 2e-4 // initialized learning rate
    , "lr_scheme": "MultiStepLR" // learning rate decay scheme
    , "lr_steps": [200000, 400000, 600000, 800000] // at which steps, decay the learining rate
    , "lr_gamma": 0.5 

    , "pixel_criterion": "l1" // "l1" | "l2", criterion
    , "pixel_weight": 1.0
    , "val_freq": 5e3 // validation frequency

    , "manual_seed": 0
    , "niter": 1e6 // total training iteration
  }

  , "logger": { // logger configurations
    "print_freq": 200
    , "save_checkpoint_freq": 5e3
  }
}
```


