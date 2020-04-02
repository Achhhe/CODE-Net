# Image Restoration :trumpet::trumpet::trumpet:(deraining ,desnowing, low-light enhancement and dehazing)

This repository is for RDL (Image Deraining with Density Estimation by Reweighting).

Codes will be published after acceptance. :smile:

<div  align="center">    
<img src="figs/derain/intro.png" width = "650"  alt="haha" align=center />   
</div>

<div  align="">    
Figure 1. Real deraining results on light, medium and heavy rain of our model, with the density estimation in the bottom (yellow: rainy inputs; blue: deraining results).
</div>

## Contents

* [Introduction](#introduction)

* [Dependencies](#dependencies)

* [Train](#train)

* [Test](#test)

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
* [Acknowledgements](#acknowledgements)

## Introduction

The task of single image deraining is an ill-posed problem and thus very challenging even with deep learning methods. Furthermore, **the presence of non-uniform rain densities** makes the problem even harder to solve. In this paper, we propose to remove raining effects by reconstructing clean rain streaks using the framework of reweighted convolutional sparse coding (CSC). Specifically, through expressing the rain streaks by the CSC model, **the rain density can be adaptively estimated via the reweighted sparsity prior**.  Experiments on synthetic and real-world data demonstrate the superiority of our methods . In addition, **we also validate that our framework can benefit other low- and high-level vision tasks in extensions**.

<br/>

<div  align="center">    
<img src="figs/rdl_net.jpg" width = "400"  alt="haha" align=center />   
</div>

<br/>

<div  align="center">    
Figure 2. Architecture of the proposed RDL.
</div>

## Dependencies
* Python 2 (Recommend to use [Anaconda](https://www.anaconda.com/distribution/#linux))
* [Pytorch 1.0.1](https://pytorch.org/)
* NVIDIA GPU + [CUDA](https://developer.nvidia.com/cuda-downloads)
* Python packages: pip install xxx

## Train
### Prepare dataset

We use 12000 and 1800 pairs of images from [DID-MDN](https://github.com/hezhangsprinter/DID-MDN) and [JORDER](http://www.icst.pku.edu.cn/struct/Projects/joint_rain_removal.html) as training set. For testing, two
commonly synthetic datasets, [Rain1200](https://github.com/hezhangsprinter/DID-MDN) and [Rain12](http://openaccess.thecvf.com/content_cvpr_2016/papers/Li_Rain_Streak_Removal_CVPR_2016_paper.pdf), and some real-world images are utilized

## Train

ToDO

## Testing

ToDO

## Results

### Rain Density Estimation (RDE) by Weights

The rain density is estimated **without any labels** in our model, instead of training an extra network in a supervised way to classify the rain density into three categories in DID-MDN [11]. Besides, thanks to the weights, our model is capable of **estimating the rain density with continuous states**, which is more suitable for real raining scenes than algorithms only classifying rain density into limited discrete states, for instance, DID-MDN.

<div  align="center">    
<img src="figs/derain/rde.jpg" width = "800"  alt="haha" align=center />   
</div>

<div  align="">    
Figure 2. A clear image (blue) and several samples (yellow) of different rain levels and corresponding RDEs.
</div>

### Qualitative Comparisons

<div  align="center">    
<img src="figs/derain/rain1200.png" width = "800"  alt="haha" align=center />   
<img src="figs/derain/rain12.jpg" width = "800"  alt="haha" align=center />    
</div>

<div  align="center">       
 On synthetic images
</div>

<div  align="center">    
<img src="figs/derain/real.png" width = "800"  alt="haha" align=center />  
</div>
 <div  align="center">
On real-world images
</div>
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

## Acknowledgements

