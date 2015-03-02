#Created by Michael Iovine
#California Academy of Mathematics and Science 
from PIL import Image 

message = raw_input('Enter a binary sring to hide: ')
binary = list(message)
rawim = raw_input('Select an input file: ')
y = int(raw_input('Select starting Y value: '))
im = Image.open(rawim)
pixel = im.load()
i = 0
x = 0
while i < len(binary):	
	r,g,b,a = im.getpixel((x,y))
	pixel[x,y] = (r+int(binary[i]), b+int(binary[i+1]), g+int(binary[i+2]), a+int(binary[i+3]))
	i += 4
	x += 1
im.save('encoded.png')