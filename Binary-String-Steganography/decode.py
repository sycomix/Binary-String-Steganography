#Created by Michael Iovine
#California Academy of Mathematics and Science 
from PIL import Image 

rawim = raw_input('Enter a file to decode: ')
im = Image.open(rawim)
pixel = im.load()
pix_x, pix_y = im.size
string = []
y = 0
def decode():
	for x in range(pix_x):
		values = len(im.getpixel((x,y)))
		if values == 3:
			r,g,b = im.getpixel((x,y))
			if r % 2 == 0:
				string.append('0')
			if r % 2 == 1:
				string.append('1')
			if g % 2 == 0:
				string.append('0')
			if g % 2 == 1:
				string.append('1')
			if b % 2 == 0:
				string.append('0')
			if b % 2 == 1:
				string.append('1')

		elif values == 4:
			r,g,b,a = im.getpixel((x,y))
			if r % 2 == 0:
				string.append('0')
			if r % 2 == 1:
				string.append('1')
			if g % 2 == 0:
				string.append('0')
			if g % 2 == 1:
				string.append('1')
			if b % 2 == 0:
				string.append('0')
			if b % 2 == 1:
				string.append('1')
			if a % 2 == 1:
				string.append('1')
			if a % 2 == 0:
				string.append('0')
while not '1' in string:
	y += 1
	string = []
	decode()
while len(string) % 8 != 0:
	string.append('0')
binary = ''.join(string) 
message = ''.join(chr(int(binary[i:i+8], 2)) for i in xrange(0, len(binary), 8))
print message