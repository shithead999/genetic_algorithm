import random, math
from rocket import Rocket
from settings import *

class Population:
	def __init__(self, c, pillars):
		self.c = c
		self.population = [Rocket(self.c, pillars) for i in range(POP_SIZE)]
		self.pillars = pillars
		self.g_index = 0
		self.maxd = 0
		self.matingPool = []

	def update(self):
		if self.g_index < FORCE_COUNT:
			for r in self.population:
				r.update(self.g_index)
		self.g_index+=1;

	def calc_fitness(self):
		self.maxd = 0 
		for r in self.population:
			r.calc_fitness()
			self.maxd = max(self.maxd, r.fitness) 
			
	def natural_selection(self):
		pass

	def generate(self):
		pass
