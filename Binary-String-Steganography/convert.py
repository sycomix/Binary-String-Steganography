#Created by Michael Iovine
#California Academy of Mathematics and Science 
from PIL import Image

rawim = raw_input('Choose an image to convert: ')
im = Image.open(rawim)
pixels = im.load()
pix_x = int(raw_input('Enter width of image: '))
pix_y = int(raw_input('Enter height of image: '))

for x in range(pix_x):
	for y in range(pix_y):
		r, g, b, a = im.getpixel((x,y))
		if r % 2 == 1:
			r = r-1 
		if g % 2 == 1:
			g = g-1
		if b % 2 == 1:
			b = b-1
		if a % 2 ==1:
			a = a-1
		pixels[x,y] = (r,g,b,a)
im.save('output.png')
			