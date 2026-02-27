# BGR and RGB
Images are typically represented as 3D arrays or tensors which is essentially a stack of matrices.
Example:

```python
import numpy as np
A (2, 2, 3) tensor: 2 matrices, each 2x3
tensor_3d = np.array([
    [[56, 183, 1], [65, 164, 0]],
    [[85, 176, 1], [44, 164, 0]]
])
```


# Grayscale image
It is a technique to get rid of color channel from the tensor for ML model to learn shapes and other things in the image without being distracted by color. It makes the image gray.


# Binary image
We use it to create a Mask, basically converting an image to "What i care about" and "What i do not".
