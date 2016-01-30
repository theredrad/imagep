from PIL import Image

class Imagep: #Image Permutation

	counter = 0

	def __init__(self, x, y ,c):
		self.img = Image.new( 'RGB', (x, y), "black")# create a new black image
		self.pixels = self.img.load() # create the pixel map
		self.colors = [(0,0,0), (255,255,255)] # create color array, black and white 
		self.colorful = c
		self.generate(0, 0)

	def generate(self, m, n):
		if(m >= self.img.size[0]):
			name = '' # I couldn't find any better way, so saving pixel rgb array as name for find certain image, but it waste process
			for w in range(self.img.size[0]):
				for z in range(self.img.size[1]):
					name = name + str(self.pixels[w,z]) # add pixel color rgb to file name
			self.img.save("tmp/" + name + ".bmp")
			self.counter += 1
			print("File #" + str(self.counter) + " saved.")
		else:
			for i in range(m, m+1):
				for j in range(n, n+1):
					if(self.colorful):
						for x in range(255):
							for y in range(255):
								for z in range(255):
									self.pixels[i,j] = (x, y , z)
									if(j+1 >= self.img.size[1]): # end of row, start from first cell of next row
										self.generate(i+1, 0) 
									else:
										self.generate(i, j+1) # next cell of row
					else:
						for c in range(len(self.colors)):
							self.pixels[i,j] = self.colors[c]
							if(j+1 >= self.img.size[1]): # end of row, start from first cell of next row
								self.generate(i+1, 0) 
							else:
								self.generate(i, j+1) # next cell of row

x = input("How many rows? \n")
y = input("How many columns? \n")
Imagep(x, y, False)