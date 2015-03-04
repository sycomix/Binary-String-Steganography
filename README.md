### Binary String Steganography
Tool to hide strings of binary in images.

### About
This script hides a message in an image by doing the following:
1.) Convert all the RGB values of the pixels in any given image to even numbers.
2.) Type in a string and convert it to binary. 
3.) Choose a Y value on the image to hide the message. 
4.) Start adding the string of binary to the RGB values. For example, if you wanted to hide '01001000', you would add 0 to the R value of the first pixel, 1 to the B value of the first pixel, and so on.
To decode a message:
1.) The decoder checks every Y value until it finds a '1'. 
2.) If an RGB value is even, it appends a '0' to your binay string. If an RGB value is odd, it appends a '1'.
3.) The binary string is converted back into ascii and printed out. 
