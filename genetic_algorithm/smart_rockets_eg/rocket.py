from settings import *
from vector import Vector
import math, random

# agent class this is similar to dna class
class Rocket:
	def __init__(self, c, pillars):
		self.c = c
		self.coor = A_START_COOR
		self.cx = None
		self.cy = None
		self.obj = self.c.create_rectangle(self.coor, outline=COLORS[1], fill=None, width=2)
		self.vel = Vector(0,0)
		self.pillars = pillars
		self.genes = []
		self.getRandGenes()
		self.alive = True
	# get random forces array
	# random.random() -> any float between 0,1
	def getRandGenes(self):
		for i in range(FORCE_COUNT):
			angle = random.random()*math.pi*2
			acc = Vector.from_angle(angle)
			acc.mult(random.random() * MAX_FORCE)
			self.genes.append(acc)

	def applyForce(self, force):
		self.vel.add(force)		

	def update(self, ind):
		if self.alive:
			coords = self.c.coords(self.obj)
			if coords[0] <= 0 or coords[2] + A_SIZE >= WIDTH or coords[1] <= 0 or coords[3] + A_SIZE > HEIGHT:
				self.alive = False 
				return
			if ((coords[0] >= TARGET_COOR[0]-TARGET_SIZE and coords[0] <= TARGET_COOR[0]+TARGET_SIZE
				and coords[1] >= TARGET_COOR[1]-TARGET_SIZE and coords[1] <= TARGET_COOR[1]+TARGET_SIZE)
				or (coords[2] >= TARGET_COOR[0]-TARGET_SIZE and coords[2] <= TARGET_COOR[0]+TARGET_SIZE
				and coords[3] >= TARGET_COOR[1]-TARGET_SIZE and coords[3] <= TARGET_COOR[1]+TARGET_SIZE)):
				self.alive = False
				return
			for pillar in self.pillars:
				if pillar.check_collide(self.obj):
					self.alive = False
					return
			self.applyForce(self.genes[ind])
			self.c.move(self.obj, self.vel.x, self.vel.y)

	def calc_fitness(self):
		pass
	@staticmethod
	def crossover_and_mutate(r1, r2, pillars):
		baby = Rocket(r1.c, pillars)
		# add code to crossover and mutate
		return baby

