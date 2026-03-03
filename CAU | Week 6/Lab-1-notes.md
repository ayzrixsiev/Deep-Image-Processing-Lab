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