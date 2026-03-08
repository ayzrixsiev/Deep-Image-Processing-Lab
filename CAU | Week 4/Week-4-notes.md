# Binary image
Binary images are images who's pixels' value is one or zero. We have two parts, ROI and background (things we do not care about). WHITE - interest, BLACK - do not care. Why they are important?
1. Reduce computational complexity.
2. Simplify image representation.
3. Improve processing speed.
4. Highlight important structures.

# Tresholding
This is a technique used to convert grayscale images into binary images.

Formula for tresholding:

1 if (x, y) >= T        
0 if (x, y) <  T

(x, y) are the grayscale pixel value on axis plane and depending on the condition it is going to be converted into 1 (ROI) or 0.

# Tresholding types, their pros and cons

**Global tresholding**    
What it is: Global tresholding takes one number and applies to all pixels, perfect for images with uniform lighting, e.g. document. But it's downside is when image has e.g. slightly dark corner it will make it completly black even if there was a detail that we might be interested in.

**Adaptive tresholding**     
What it is: Instead of one treshold for the whole image, computer devides image into neighborhoods (blocks) and calculates a different treshold value for each of them. Best for images with uneven lighting. But it may falls short in areas where there is no really ROI object but it is still going to try to find it and make it white because of noise.

        T(local for the certain area) = Mean of Neighborhood(simple mean or Gaussian-weighted mean) - C(constant value, the higher it is the more pixels become black, the smaller it is the smaller it becomes).

**Otsu's tresholding:**
What it is: It is also uses one global value for each pixel but calculates it based on the image's histogram (two mountains. dark and black). Best for bimodal images (those which have clear distinction between foreground and background). Donwside is same as in global tresholding, it may fail if light and dark varies too much.  


# Gamma correction
This is a technique to adjust the brightness of an image. Gamma < 1.0 makes image brighter, gamma > 1.0 make image darker.

# Contrast Stretching
This is a technique used to expand the range of intensity levels in image. If an image only uses a narrow range of colors (e.g., all pixels are between 50 and 150), it will look dull or "foggy." It maps the lowest pixel value in your image to 0 (black) and the highest pixel value to 255 (white), stretching everything in between to fill the available space .
