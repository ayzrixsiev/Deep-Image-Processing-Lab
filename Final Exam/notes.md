# Chapter 1: Spatial Filtering - Smoothing Filters

### Spatial filtering is a technique of sliding window (mask) over the image, computing new center value based on it's neighbors.

**Box filtering** is one of the implementations of this technique, we change each pixel by computing average of all the pixels. We must normilize this filter in order to avoid sum > 1, which will make image too bright or sum < 1 which makes image too dark. If we make value. 

Example image:      
[ 10  20  30  40  50 ]      
[ 15  25  35  45  55 ]      
[ 20  30  40  50  60 ]      
[ 25  35  45  55  65 ]      
[ 30  40  50  60  70 ]      

Apply 3x3 box filter        
[ 25  35  45 ]      
[ 30  40  50 ]      
[ 35  45  55 ]      

Calculate the average:      
Sum = 25+35+45+30+40+50+35+45+55 = 360      
Average = 360/9 = 40        
The center pixel stays 40       

**Kernel size** directly affects blurring effect. The larger the kernel, the more local detail gets averaged out.
3×3 kernel: Averages over 9 pixels (small neighborhood)     
21×21 kernel: Averages over 441 pixels (huge neighborhood)      

**Gaussian filter** instead of giving equal weight to all neigbors like box filter (kernel consists from 1s), gaussian gives more weight to closer pixels and less weight to farther pixels. The kernel should always be odd, to have a clear center.

**Circular Symmetry** this means the filter treats equally all pixels regardless direction. Box does not follow the rule, while gaussian does.


