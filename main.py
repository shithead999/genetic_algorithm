from DNA import DNA
from population import Population

# variables
phrase = "Out of the box."
pop_size = 10

def main():
	p = Population(phrase, pop_size)
	p.calc_fitness()
	print("Best Fitness:", str(p.best_fitness))
	print("Best Fit DNA:", p.best_fit_dna.get_str())
	p.show_pop()


if __name__ == "__main__":
	main()
