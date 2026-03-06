# Binary image
Binary images are images who's pixels' value is one or zero. We have two parts, ROI and background (things we do not care about).

# Tresholding
This is a technique used to convert grayscale images into binary images.

Formula for tresholding:

1 if (x, y) >= T        
0 if (x, y) <  T

(x, y) are the grayscale pixel value on axis plane and depending on the condition it is going to be converted into 1 (ROI) or 0.

# Tresholding types

Global tresholding: When we are using one value for all the pixels on the image, fast and simple and usually for predictive (documents, images with uniform lightning) data without illuminations.

Adaptive tresholding: When we use different treshold values on different image areas. We use neighborhood statistics (mean or Gaussian-weighted average). We use it for uneven lighting conditions, medical images, real world surveillance images.

Otsu's tresholding: Treshold selected automatically by doing math. Good for most of the data.
