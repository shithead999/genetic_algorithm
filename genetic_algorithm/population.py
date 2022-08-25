from DNA import DNA
import random
import math

random.seed(27)


class Population:
	def __init__(self, mrate, phrase, size, ui):
		self.population = []
		self.ui = ui
		self.size = size
		self.best_fit_dna = None
		self.best_fitness = -1
		self.phrase = phrase
		self.matingPool = []
		self.generation = 1
		self.mutation_rate = mrate
		self.create_random_population()
		self.calc_fitness()
		self.running = True

	def crossover(self, parent_a, parent_b):
		# Approch 1: n = len(self.phrase)//2

		baby = DNA(self.phrase)
		for i in range(len(self.phrase)):
			baby.genes[i] = random.choice([parent_a.genes[i],parent_b.genes[i]])
		return baby

	def calc_fitness(self):
		for i in self.population:
			i.calc_fitness()
			if i.fitness > self.best_fitness:
				self.best_fitness = i.fitness
				self.best_fit_dna = i
				self.ui.best_phrase.set('"'+self.best_fit_dna.get_str()+'"')
				if self.best_fit_dna.get_str() == self.phrase:
					self.running = False 

	def natural_selection(self):
		self.matingPool = []
		for dna in self.population:
			freq = math.floor((dna.fitness / self.best_fitness) * 100)
			for i in range(freq):
				self.matingPool.append(dna)

	def create_random_population(self):
		for i in range(self.size):
			d = DNA(self.phrase)
			self.population.append(d)

	def generate(self):
		self.population = [] # killing the previous population
		for i in range(self.size):
			parent_a = random.choice(self.matingPool)
			parent_b = random.choice(self.matingPool)
			baby = self.crossover(parent_a, parent_b)
			baby.mutate(self.mutation_rate)
			self.population.append(baby)
		self.generation += 1

	def show_pop(self):
		self.ui.l1.set(self.population[0].get_str())
		self.ui.l2.set(self.population[1].get_str())
		self.ui.l3.set(self.population[2].get_str())
		self.ui.l4.set(self.population[3].get_str())
		self.ui.l5.set(self.population[4].get_str())

