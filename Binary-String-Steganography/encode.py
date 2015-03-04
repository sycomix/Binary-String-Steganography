#Created by Michael Iovine
#California Academy of Mathematics and Science 
from PIL import Image 
rawim = raw_input('Choose a file to encode: ')
im = Image.open(rawim)
def convert():
	pixels = im.load()
	pix_x, pix_y = im.size
	for x in range(pix_x):
		for y in range(pix_y):
			values = im.getpixel((x,y))
			if len(values) == 4:
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
			elif len(values) == 3:
				r,g,b = im.getpixel((x,y))
				if r % 2 == 1:
					r = r-1 
				if g % 2 == 1:
					g = g-1
				if b % 2 == 1:
					b = b-1
				pixels[x,y] = (r,g,b)
convert()
message = raw_input('Enter a sring to hide: ')
binary_str = ''.join(format(ord(a),'b').zfill(8) for a in message)
binary = list(binary_str)
y = int(raw_input('Select starting Y value: '))
pixel = im.load()
i = 0
x = 0
while i < len(binary):
	values = len(im.getpixel((x,y)))
	if values == 4:
		while len(binary) % 4 != 0:
			binary.append('0')
		r,g,b,a = im.getpixel((x,y))
		pixel[x,y] = (r+int(binary[i]), b+int(binary[i+1]), g+int(binary[i+2]), a+int(binary[i+3]))
		i += 4
		x += 1
	elif values == 3:
		while len(binary) % 3 != 0:
			binary.append('0')
		r,g,b = im.getpixel((x,y))
		pixel[x,y] = (r+int(binary[i]), b+int(binary[i+1]), g+int(binary[i+2]))
		i += 3
		x += 1
im.save('encoded.png')