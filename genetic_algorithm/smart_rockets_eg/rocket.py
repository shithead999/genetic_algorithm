from settings import *
from vector import Vector
import math, random

class Rocket:
	def __init__(self, c):
		self.c = c
		self.coor = A_START_COOR
		self.cx = None
		self.cy = None
		self.obj = self.c.create_oval(self.coor, outline="black", fill=None, width=2)
		self.vel = Vector(0,0)
		self.genes = []
		self.getRandGenes()

	def getRandGenes(self):
		for i in range(FORCE_COUNT):
			angle = random.random()*math.pi*2
			acc = Vector.from_angle(angle)
			acc.mult(1 + random.random()*2)
			self.genes.append(acc)

	def applyForce(self, force):
		self.vel.add(force)		

	def update(self):
		if len(self.genes):
			self.applyForce(self.genes.pop())
			self.c.move(self.obj, self.vel.x, self.vel.y)