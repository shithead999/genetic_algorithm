from DNA import DNA
import math

class Population:
	def __init__(self, phrase: str, size: int):
		self.population = []
		self.size = size
		self.best_fit_dna = None
		self.best_fitness = -1
		self.phrase = phrase
		self.matingPool = []
		self.create_random_population()
		self.calc_fitness()

	def calc_fitness(self):
		for i in self.population:
			i.calc_fitness()
			if i.fitness > self.best_fitness:
				self.best_fitness = i.fitness
				self.best_fit_dna = i
		self.create_mating_pool()

	def create_mating_pool(self):
		self.matingPool = []
		for dna in self.population:
			freq = math.floor((dna.fitness / self.best_fitness) * 100)
			print("freq: " + str(freq), ", " + dna.get_str())
			print()
			for i in range(freq):
				self.matingPool.append(dna)

	def create_random_population(self):
		for i in range(self.size):
			d = DNA(self.phrase)
			self.population.append(d)

	def natural_selection(self):
		pass

	def show_pop(self):
		print()
		cnt = 0
		for dna in self.population:
			print("|" + dna.get_str() + "|")
			cnt+=1
			if cnt == 10:
				break;

