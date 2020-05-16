# Image Restoration :trumpet::trumpet::trumpet:(deraining ,desnowing, low-light enhancement and dehazing)

This repository is for CODE-Net (Single Image Deraining with Continuous Rain Density Estimation).

Codes will be released soon :smile:

<div  align="center">    
<img src="figs/derain/intro.png" width = "650"  alt="haha" align=center />   
</div>

<div  align="">    
Figure 1. Deraining results on real images with light, medium and heavy rain (top) by SPANet (middle) and by our method (bottom).  Our method could produce more pleasant results. The rain density of each image is estimated by our method and indicated in read.
</div>

## Contents

* [Introduction](#introduction)

* [Results](#results)
  * [Rain Density Estimation (RDE) by Weights](#rain-density-estimation-(rde)-by-weights)
  * [Qualitative Comparisons](#qualitative-comparisons)
  * [Quantitative Comparisons](#quantitative-comparisons)
* [Extensions](#extensions)
  * [Low-level ](#low-level )
    * [Desnowing](#desnowing)
    * [Low-light Enhancement](#low-light-enhancement)
    * [Dehazing](#dehazing)
  * [High-level](#high-level)

## Introduction

Single image deraining (SIDR) often suffers from over/under deraining due to **the nonuniformity of rain densities and the variety of raindrop scales**. In this paper, we propose a **co**ntinuous **de**nsity guided network (CODE-Net) for SIDR. Particularly, it is composed of  a rain streaks extractor and a denoiser, where the convolutional sparse coding (CSC) is exploited to filter out noises from the extracted rain streaks. Inspired by  the reweighted iterative soft-threshold for CSC, we address the problem of continuous rain density estimation by learning the weights with channel attention blocks from sparse codes. We further exploit **a multiscale strategy to depict rain streaks appearing at different scales**. Experiments on **synthetic and real-world** data demonstrate the superiority of our methods over recent state-of-the-arts, in terms of both quantitative and qualitative results. Additionally, instead of quantizing rain density with several levels, our CODE-Net can provide **continuous-valued estimations of rain densities, which is more desirable in real applications**.

<div  align="center">    
<img src="figs/rdl_net.jpg" width = "400"  alt="haha" align=center />   
</div>

<div  align="center">    
Figure 2. Architecture of the proposed CODE-Net.
</div>

## Results

### Rain Density Estimation (RDE) by Weights

The rain density is estimated **without any labels** in our model, instead of training an extra network in a supervised way to classify the rain density into three categories in DID-MDN. Besides, thanks to the weights, our model is capable of **estimating the rain density with continuous states**, which is more suitable for real raining scenes than algorithms only classifying rain density into limited discrete states, for instance, DID-MDN.

<div  align="center">    
<img src="figs/derain/rde.jpg" width = "800"  alt="haha" align=center />   
</div>

<div  align="">    
Figure 3. A clear image (blue) and several samples (yellow) of different rain levels and corresponding RDEs.
</div>

### Qualitative Comparisons

<div  align="center">    
<img src="figs/derain/rain1200.png" width = "800"  alt="haha" align=center />   
<img src="figs/derain/rain12.jpg" width = "800"  alt="haha" align=center />       
</div>

<div  align="center">       
 Qualitative comparisons (PSNR, SSIM) of images from Rain1200 and Rain12.
</div>

<div  align="center">    
<img src="figs/derain/real1.png" width = "800"  alt="haha" align=center />  
<img src="figs/derain/real2.png" width = "800"  alt="haha" align=center />
</div>

 <div  align="center">
Qualitative comparisons of real-world images, with the corresponding RDE calculated by our method.
</div>

<div  align="center">    
<img src="figs/derain/real5.png" width = "800"  alt="haha" align=center />  
</div>

 <div  align="center">
More qualitative comparisons of real-world images.
</div>

**More deraining results on Rain1200/Rain12/Testing1000/RealImages  could be found in [BaiduNetdisk](https://pan.baidu.com/s/1crBm7pbjXfg3MiiCDbxWzA) (psw:nhra)**


### Quantitative Comparisons 

<div  align="center">    
<img src="figs/derain/tables.png" width = "800"  alt="haha" align=center />   
</div>

## Extensions

### Low-level vision tasks 

#### Desnowing

<div  align="center">    
<img src="figs/desnow/desnow4.gif" width = "253"  alt="haha" align=center />
<img src="figs/desnow/desnow5.gif" width = "250" height = "190"  alt="haha" align=center />
<img src="figs/desnow/desnow12.gif" width = "250"  alt="haha" align=center />  
</div>

<div  align="center">    
<img src="figs/desnow/desnow2.gif" width = "250"  alt="haha" align=center />
<img src="figs/desnow/desnow9.gif" width = "250" alt="haha" align=center />
<img src="figs/desnow/desnow3.gif" width = "250"  alt="haha" align=center />  
</div>

<div  align="center">    
<img src="figs/desnow/desnow7.gif" width = "250" height="189"  alt="haha" align=center />
<img src="figs/desnow/desnow22.gif" width = "250" height = "190"  alt="haha" align=center />
<img src="figs/desnow/desnow10.gif" width = "250" height="190"  alt="haha" align=center />  
</div>

[More desnowing results](./figs/desnow/)

#### Low-light enhancement

<div  align="center">    
<img src="figs/lowlight/lowlight18.gif" width = "250"   alt="haha" align=center />
<img src="figs/lowlight/lowlight19.gif" width = "250"   alt="haha" align=center />
<img src="figs/lowlight/lowlight20.gif" width = "250"   alt="haha" align=center />  
</div>

<div  align="center">    
<img src="figs/lowlight/lowlight8.gif" width = "250"   alt="haha" align=center />
<img src="figs/lowlight/lowlight3.gif" width = "250"   alt="haha" align=center />
<img src="figs/lowlight/lowlight9.gif" width = "250"   alt="haha" align=center />  
</div>

<div  align="center">    
<img src="figs/lowlight/lowlight24.gif" width = "250"   alt="haha" align=center />
<img src="figs/lowlight/lowlight25.gif" width = "250"   alt="haha" align=center />
<img src="figs/lowlight/lowlight26.gif" width = "250"   alt="haha" align=center />  
</div>

<div  align="center">    
<img src="figs/lowlight/lowlight14.gif" width = "251"   alt="haha" align=center />
<img src="figs/lowlight/lowlight10.gif" width = "250" height="185"  alt="haha" align=center />
<img src="figs/lowlight/lowlight6.gif" width = "250"   alt="haha" align=center />  
</div>

[More low-light enhancement results](./figs/lowlight/)

#### Dehazing

<div  align="center">    
<img src="figs/dehaze/dehaze2.gif" width = "250" height="190"  alt="haha" align=center />
<img src="figs/dehaze/dehaze9.gif" width = "250" height="190"  alt="haha" align=center />
<img src="figs/dehaze/dehaze10.gif" width = "250" height="190"  alt="haha" align=center />
</div>

<div  align="center">    
<img src="figs/dehaze/dehaze5.gif" width = "250" height="190"  alt="haha" align=center />
<img src="figs/dehaze/dehaze1.gif" width = "250" height="190"  alt="haha" align=center />
<img src="figs/dehaze/dehaze12.gif" width = "250" height="190"  alt="haha" align=center />
</div>

<div  align="center">    
<img src="figs/dehaze/dehaze7.gif" width = "250" height="190"  alt="haha" align=center />
<img src="figs/dehaze/dehaze3.gif" width = "250" height="190"  alt="haha" align=center />
<img src="figs/dehaze/dehaze4.gif" width = "250" height="190"  alt="haha" align=center />
</div>

[More deshazing results](./figs/dehaze/)

### High-level vision tasks

Object detection results with/without deraining. The labels and corresponding confidences are both given by [Google Vision API](https://cloud.google.com/vision/). (*left: rainy inputs; right: deraining results*)

<div  align="center">    
<img src="figs/high-level/hl2.png" width = "800"   alt="haha" align=center />
<img src="figs/high-level/hl3.png" width = "800"  alt="haha" align=center />  
<img src="figs/high-level/hl4.png" width = "800"  alt="haha" align=center />  
<img src="figs/high-level/hl1.png" width = "800"  alt="haha" align=center /> 
</div>

**All of the above verify the effectiveness of our proposed method.**