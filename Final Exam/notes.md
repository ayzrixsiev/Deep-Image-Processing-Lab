# Chapter 1: Spatial Filtering - Smoothing Filters

## Spatial filtering
It is a technique of sliding window (mask) over the image, computing new center value based on it's neighbors.

### Box filtering       
It is one of the implementations of this technique, we change each pixel by computing average of all the pixels. We must normilize this filter in order to avoid sum > 1, which will make image too bright or sum < 1 which makes image too dark. If we make value sum = 1, we are good. 

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

### Gaussian filter
Instead of giving equal weight to all neigbors like box filter (kernel consists from 1s), gaussian gives more weight to closer pixels and less weight to farther pixels. The kernel should always be odd, to have a clear center.

**Circular Symmetry** this means the filter treats equally all pixels regardless direction. Box does not follow the rule, while gaussian does.

**Padding methods**, when we reach borders of images with kernel, some of our neighbors will be outside of the box, we need to decide what to do with them.

    1. Zero padding. When we add zeroes to the borders.
    Original:  [ 100  120  140 ]
    Padded:    [ 0  0  100  120  140  0  0 ]
    Effect: We create dark borderes and reduce average near the borders

    2. Mirror padding. When we reflect the pixels of images
    Original:  [ 100  120  140 ]
    Padded:    [ 140  120  100  120  140  120  100 ]
    Effect: We reflect image symetrically, and hence have better results.

    3. Replicate. When we extend the image's details.
    Original:  [ 100  120  140 ]
    Padded:    [ 100  100  100  120  140  140  140 ]
    Effect: We extend edge values. But we can create slight discontinuities.

    Best practice: Mirror padding for the most cases, because it maintains natural transitions.


### Median filtering
Unlike Gaussian and box fileting, where we use average to find a center pixel, here we use order statictics.
We get all the neighbors, sort them in order, and take median value (center value), replace center with median.

Example: Removing Salt-and-Pepper Noise
Neighborhood with impulse noise:
[ 12  15  14 ]
[ 13  255  15 ]  ← Center pixel is corrupted (255 = white noise)
[ 16  14  13 ]
Step 1: Extract values: [12, 15, 14, 13, 255, 15, 16, 14, 13]
Step 2: Sort: [12, 13, 13, 14, 14, 15, 15, 16, 255]
Step 3: Median = 14 (the middle value)
Result: The noise spike (255) is completely removed! The median is 14.

**Salt-and-Pepper noise** is when we have random black and white dots on images

![Salt-and-pepper](../data/images/saltandpepper.png)

To solve this problem, best option is median filter. First of all those big numbers (black 0 and white 255 dots) go to the beginning or the end of the ordered list. Second, median is a "typical" pixel on the image, so almost no changes is visible.

**Illumination / shading correction** this is a certain image, that has illumination (Imagine an image with a landscape, with stones and trees, besides that we also have one big mountain hill, object like stones and trees has a brightness transition very quickly, but hill this is like a massive object, it starts bright on the left and gets slightly darker on the right, this change is "slow" because it takes 100 or 200 pixels to notice the difference). Which means a bad lightning, for example it causes problem when we try to apply tresholding. Solution is to apply gaussian blur.

When you apply a massive Gaussian Filter (like 101x101):
You are telling the computer to blur everything so much that the "mountains" (the objects/details) disappear, leaving only the "giant hill" (the lighting pattern). After that we resulted image and subtract it from original one.

## Sharpening Filters

### High pass filters vs Low Pass filters

We have two main brightness domains in the images:      
Low frequencies - when brightness changes slowly (like in large objects).        
High frequencies - when brightness changes fast (lines, new objects).        

**Low pass filter** - helps us smooth those fast fast changing brightness parts, creating a blur effect. (deals with high frequencies).      
**High pass filters** - keep fast changing details, and get rid off "slow" parts to sharpen the image. (deals with low frequencies).      


### First-Order Derivatives (Sobel)

**Derivative** measures the rate of change of intensity. Formula: f'(x) = f(x+1) - f(x).         
Example:        
Intensity profile: [ 100  100  100  150  200  200  200 ]        
First derivative:  [   0    0   50   50    0    0      ]    

Why First Derivatives Give Thick Edges? If we take an example of this edge: [ 50  50  60  80  120  160  180  190  200  200 ].

The intensity changes slowly. But deravitive can calculate only the change of two pixels at a time, meaning how much current pixel changed from previous one? Hence each check it marks a change as a new edge, as a result we get thick line.

### First-Order Gradient Operators

**Roberts Cross Operator**    

     Gx = [ 1   0 ]        Gy = [ 0   1 ]      
          [ 0  -1 ]             [-1   0 ]                      

To detect diagonal edges, very sensitive to noise.       

**Sobel operator**      

     Gx = [-1  0  1 ]      Gy = [-1 -2 -1 ]      
          [-2  0  2 ]           [ 0  0  0 ]      
          [-1  0  1 ]           [ 1  2  1 ]      

To detect horizontal and vertical edges, has it's own smoothing effect (look at 1, 2, 1). good for noisy images.     

###  Second-Order Derivatives (Laplacian)

Formula: f''(x) = f(x+1) + f(x-1) - 2×f(x)

This gives us more precise deravitive localization. Because of the concept named: Zero crossing, which means we can find a center of the edge creating a precise location. We use the concept of - and +.

**Laplacian** this is a technique where we extract edges using second deravitive.
The normal laplacian kernel looks the following way:        

[1   1    1]                
[1  -8    1]             
[1   1    1]                  

Example image with a spike:        
[ 100  100  100 ]        
[ 100  150  100 ]  ← Edge pixel         
[ 100  100  100 ]        

     Process:       
     1. Multiply neighbors: 100 * 8 = 800 (get the sum of all neighbors)      
     2. Multiply center: 150 * (-8) = -1200          
     3. Sum them up: 800 + (-1200) = -400 (if it is not zero we found a detail)      

This is how we can identify details/edges and use this resulted image to enhance original image details.
**Sharpened image = Original - Laplacian**      

Second deravitive is much sensitive to the noise since it amplifies the noise. For example:

Clean signal:     [ 100  100  100  100 ]               
Noisy signal:     [ 100   95  105  100 ]               

First derivative:  [ -5   10   -5      ]          
Second derivative: [ 15  -15   5       ]  ← Larger amplification!


Solution: Smooth Before Sharpening      

Apply Gaussian smoothing to reduce noise          
Then apply Laplacian or other sharpening          
This reduces false edge detections      

### Unsharp masking
This is another process of getting details on the image. First we blur the image using low pass filter (Gaussian blur) and get rid off all sharp details, once that happens we successfully isolate low frequency details. Second step is to subtract this blur from original image, to isolate high frequency details (shapry details), this is called: mask image. Third step is to add this mask to the original image to enhance details.

1. Blur orig image to kill sharp details
2. Subtract this blur from orig image to isolate sharp details.
3. Add this mask to orig image to enhace sharp details.

Formula: Sharpened = Orig + Mask

### Highboost filtering
This is an addition to the unsharp masking. Which can be added to the formula: Sharpened = Orig + **k** + Mask
It amplifies high freq details. Which then results in a sharper overall image, aka crispier.

**Point detection** we use laplacian to find "spikes" in the images, and when there is a brighter spot we get negative value, while if it is dark we get positive number. But we need to identify whether it is a spot or not regardless of it's color, so we take an absolute value of it. After that we set up a certain threshold, to idetify whether that is really a point or just very tiny unecessary detail.

**Line detection** is where we use different kernels to detect lines in different directions on the image.
     [ -1  -1  -1 ]      
     [  2   2   2 ] <- Horizontal detection       
     [ -1  -1  -1 ]      

     [ -1   2  -1 ]      
     [ -1   2  -1 ] <- Vertical detection         
     [ -1   2  -1 ]           

     [  2  -1  -1 ]      
     [ -1   2  -1 ] <- Diagonal X       
     [ -1  -1   2 ]      

     [ -1  -1   2 ]      
     [ -1   2  -1 ] <- Diagonal Y       
     [  2  -1  -1 ]      


# Summary

**We have several processes that we can do over the image**           
**1. Smoothing image, preprocessing**             
**2. Identifying different types of details**               

## 1. Smoothing images
We have a concept called spatial filtering. Which means we design a certain kernel and slide it over the image to change pixels values based on our goal and it each pixel's neighbors.

     We have four main smoothing kernel filters AKA Low pass filters that gets rid off high frequencies by blurring an image: 
     1. Box filter.      
     2. Gaussian filter.      
     3. Median filter.        
   
1. ### Box filter is the process of getting average of surrounding pixels and then replacing center with that value to smooth to image. This is good for real time video processing, because we just take an average, speed matters more than quality
2. ### Gaussian filter is does the same thing by taking average, but it does not treat pixels the same. Pixels (neighbors) that are closer to the center are likely the part of the same object, hence they get a higher weight and in the end better visual results than box filter. This is a solid way to preprocess an image for edge detections.
3. ### Median filter is where we use different math, we use order statistics, we slide a kernel over the image, usually 3x3 or 5x5, make an array of those images, order them in ascending order find a median and replace center with it. This filter is very good for salt and pepper images, which has big and a lot of spikes/dots on the image (255 or 0).


**Key concepts to remember about kernels**
1. Size matter. If kernel is small, it is going to take a smaller average, which results in smaller changes and keeping more details, while bigger kernel averages more pixels and have a bigger impact, which means image will be more blurred.
2. Circular symmetry means that we treat all pixels equally regrdless of direction. Box filter does not follow this rule because it is a square which means it stretches more to the edges, while Gaussian does follow the rule because it is more round like kernel.
3. Padding methods, when we slide a kernel over the image, sometimes kernel goes off the borders, and we need to add some pixels to the image to cover it. We have three main ways of doing it. First one is to add zeroes, good for images that already have black background or need a consistent input size like in CNN model. Second is mirroring pixels, meaning copy the pixels of an image near the border, helps us create more natural reult and good for image editing. Third is replicating, meaning we try to extend the details of the image, if we have a stone near the edge, we make stone bigger by making it wider for example, but this process can cause discontinuities, it can look "stretched", good for e.g medical image where we care exact brightness and details, without new fake patterns that can occur when we use mirror.


## 2. Edge detection, details extraction

     We have three High pass filters for sharpening images, meaning extracting details:
     1. Sobel.
     2. Laplacian.
     3. Unsharp masking + Highboost.

To understand how we extract the details, we first need to grasp the concept of Derivatives. We have two types of them:
First derivative and second derivative, both measures the rate of intensity change in images.       

**First derivative** is measures the difference between two pixels. It asks a question "How much current pixel's value changed from previous one".          
Example:       
[100, 100, 150, 200, 200, 200]          
[  0,  50,  50,   0,   0,   0]          
As you can see we identified from which point diff appeared and where exactly that diff happened. But for computer this is not ideal, since it does not know exactly where the edge is, first 50 or second 50, hence it takes both, as a result we have thick lines.

**Second derivative** is a measurement of change of the first deravitive. In our case:              
[  0,  50,  0,  -50,  0]           
This is called zero crossing. The point between + and - is the center of the edge.        
As you can see second der is better when it comes to more accurate edge detection.



*Sobel* is the representation of the 1st deravitive.  

     Gx = [-1  0  1 ]      Gy = [-1 -2 -1 ]      
          [-2  0  2 ]           [ 0  0  0 ]      
          [-1  0  1 ]           [ 1  2  1 ]       
We are looking for the difference in this non zero parts of the kernel by summing them. Thick lines. We need to apply both direction.

*Laplacian* is the representation of the 2nd deravitive.
     [1   1    1]                
     [1  -8    1]             
     [1   1    1]   
We are summing all teh neighbor pixels and then subtracting it from the center to see whether there is a diff. We have here cyclic symmetry, because we do not care about direction.


*Unsharp masking* is another approach to extract edges and details. First we blur the image (with gaussian) and leave it only with low freq details. Then we subtract this image from original, and create mask with high freq details, which then is added to the original image to enhance the details/edges.       
Formula: original + (original - blurred) or original + mask. In addition to this formula we also have something called highboost, which amplifies high freq details the following way: original + k * mask. Depending on k value we can get crispier, more visible details in the image. 