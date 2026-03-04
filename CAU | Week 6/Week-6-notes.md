# Convolution
If the pixels above me and below me are the same, I'll output zero. If they are different, I will light up!".
The main job is to find whether there an image is one solid color, is there any sudden changes in the brightness and color.

$$\text{Image} = \begin{bmatrix} 
50 & 50 & 50 \\
50 & 50 & 50 \\
200 & 200 & 200 \\
200 & 200 & 200 
\end{bmatrix}$$

$$\text{Sobel Kernel} = \begin{bmatrix} 
1 & 2 & 1 \\
0 & 0 & 0 \\
-1 & -2 & -1 
\end{bmatrix}$$

The Math at the Edge:     
Top Row: (1 * 50) + (2 * 50) + (1 * 50) = 200      
Middle Row: (0 * 50) + (0 * 50) + (0 * 50) = 0         
Bottom Row: (-1 * 200) + (-2 * 200) + (-1 * 200) = -800        
Total Result: 200 + 0 + (-800) = -600            


$$\text{Box Kernel} = \begin{bmatrix}
0.11 & 0.11 & 0.11 \\
0.11 & 0.11 & 0.11 \\
0.11 & 0.11 & 0.11
\end{bmatrix}$$

$$\text{Image} = \begin{bmatrix}
50 & 50 & 50 \\
50 & 50 & 50 \\
200 & 200 & 200
\end{bmatrix}$$

The Math:      
Top Row: (0.11 * 50) + (0.11 * 50) + (0.11 * 50) = 16.5         
Middle Row: (0.11 * 50) + (0.11 * 50) + (0.11 * 50) = 16.5         
Bottom Row: (0.11 * 200) + (0.11 * 200) + (0.11 * 200) = 66     
Total Result (Sum): 16.5 + 16.5 + 66 = 99


# Histogram Equalization
Assume we have an image and if it is too dark or "размыто", it's pixels are crowded in one small part of the histogram. and this function makes sure that we have pixels spread across entire range in 0-255. It does it by automatically calculating the best alpha for each image part. If we have a poor lightened image, equalizationHist() can imrpove it since it makes values spread across a whole range without being focused on one set of colors.

# Gaussian Blur
Digital images usually have a lot of random tiny bright pixels AKA noise, so when we apply any kernel it is going so think that every those tiny pixels is a noise and edge and this is why we use Gaussian blur, it helps us "melt" that noises and edges so that we can apply our kernels after it. The process: We define a kernel (window) with a certain size e.g. 3x3, 5x5, 11x11 and Sigma value that responsible for how aggressive we will melt the noise, when we apply this kernel to the image it traverses through each pixel, and the current pixel that we are looking at called center, and this center has it's own neighbors (pixels near the center, the amount of neighbors we will look at depends on the kernel size), for the center and the neighbors we assign "weigths", center has the higest weight (meaning less melting is applied to it, e.g 0.40 weight means keep 40% of the color of this image, while neighbors will may have weights like 0.12, 0.06 and etc). The formula looks the following way; 250 * 0.40 = 100 where 250 is the pixel original value + 100 (neighbor value) * 0.60 = 60, which gives us = 160, this is the new value of a center! It is no longer bright it is more smoother and softer (blurred). Note if pixels are similar nothing will change but if the center is different from other pixels than it will be changed.

# Unsharp masking
This is the process of getting an image and it's blurred version (which we got using Gaussian Blur) and subtract from each other image - blurred_image. By taking the Original and subtracting the Blur, you are basically saying: "Keep only the things that the blur destroyed." What did the blur destroy? The sharp edges and noise.

Step 1 (Blur): We hide the sharp stuff.

Step 2 (Subtract): We find out exactly what was hidden (the edges).

Step 3 (Add): We "boost" the original image by giving it a double dose of its own edges.