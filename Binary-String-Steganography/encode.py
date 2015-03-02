#Created by Michael Iovine
#California Academy of Mathematics and Science 
from PIL import Image

message = raw_input('Enter a string of binary: ')
binary = list(message)
binary.insert(0,4)
binary.insert(1,2)
rawim = raw_input('Select an input file: ')
y = int(raw_input('Select starting Y value: '))
im = Image.open(rawim)
pixel = im.load()
i = 0
x = 0
while i < len(binary):	
	r,g,b = im.getpixel((x,y))
	pixel[x,y] = (r+int(binary[i]), b+int(binary[i+1]), g+int(binary[i+2]))
	i += 3
	x += 1
im.save('encoded.png')