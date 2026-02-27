# Bitwise operations
These are pixel level operations that uses Masks to target a specific part of an image, using binary logic (AND, OR, XOR, NOT). Mask is a certain region that we define that consists of binary numbers of 0s and 1s, aka RIO - region of interest. Where 0 is the part we are not interested in and 1 is our interest


| Operation | Logic | Result |
| --- | --- | --- |
| **AND** | `Both must be white` | Only the area where the square and ellipse **overlap** remains. |
| **OR** | `Either can be white` | Both shapes are combined into one large white area. |
| **XOR** | `Only one is white` | Keeps both shapes, but the area where they overlap turns **black**. |
| **NOT** | `Invert` | Turns the white square into a black square with a white background. |