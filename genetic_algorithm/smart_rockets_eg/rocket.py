from settings import *
from vector import Vector
import math, random

# agent class this is similar to dna class
class Rocket:
	def __init__(self, c):
		self.c = c
		self.coor = A_START_COOR
		self.cx = None
		self.cy = None
		self.obj = self.c.create_rectangle(self.coor, outline="black", fill=None, width=2)
		self.vel = Vector(0,0)
		self.genes = []
		self.getRandGenes()

	# get random forces array
	def getRandGenes(self):
		for i in range(FORCE_COUNT):
			angle = random.random()*math.pi*2
			acc = Vector.from_angle(angle)
			acc.mult(1 + random.random()*MAX_FORCE)
			self.genes.append(acc)

	def applyForce(self, force):
		self.vel.add(force)		

	def update(self, ind):
		self.applyForce(self.genes[ind])
		self.c.move(self.obj, self.vel.x, self.vel.y)