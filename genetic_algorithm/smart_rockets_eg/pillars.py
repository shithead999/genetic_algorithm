from settings import *

class Pillar:
	def __init__(self, c, x, y, width, height):
		self.c = c
		self.width = width
		self.height = height
		self.coors = [x,y,x+width, y+height]
		self.obj = self.c.create_rectangle(self.coors, outline=None, fill=COLORS[2], width=0)

	def check_collide(self, object):
	 #    rect1.x < rect2.x + rect2.w &&
	 #    rect1.x + rect1.w > rect2.x &&
	 #    rect1.y < rect2.y + rect2.h &&
	 #    rect1.h + rect1.y > rect2.y
		tc = self.c.coords(object)
			
		if (tc[0] < self.coors[0] + self.width and 
			tc[0] + A_SIZE > self.coors[0] and
			tc[1] < self.coors[1] + self.height and 
		A_SIZE+tc[1] > self.coors[1]):
			return True