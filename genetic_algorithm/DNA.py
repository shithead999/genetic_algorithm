import random
import string

letters = string.ascii_lowercase + string.ascii_uppercase + "." + " " + "," 
random.seed(27)


class DNA:
	def __init__(self, phrase: str):
		self.genes = [] # array of charachters
		self.phrase = phrase
		self.generate_random_genes()
		self.fitness = 0

	def generate_random_genes(self):
		for _ in range(len(self.phrase)):
			ch = random.choice(letters)
			self.genes.append(ch)

	def calc_fitness(self):
		self.fitness = 0
		for i in range(len(self.phrase)):
			if self.genes[i] == self.phrase[i]:
				self.fitness += 1
		self.fitness = self.fitness/len(self.phrase)

	def get_str(self):
		return ''.join(self.genes)

	def mutate(self, mutation_rate):
		for i in range(len(self.phrase)):
			if random.random() < mutation_rate:
				self.genes[i] = random.choice(letters)
