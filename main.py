from DNA import DNA
from population import Population
import time
from tkinter import Tk
from ui import App
import math

# variables
phrase = "Switch to God Mode."
pop_size = 1000
mutation_rate = 0.01

def main():
	win = Tk()
	app = App(win)
	win.title("Genetic Algorithm")
	p = Population(mutation_rate, phrase, pop_size, app)
	while p.running:
		win.update()
		p.calc_fitness()
		p.natural_selection()
		p.generate()
		app.best_fit.set("Best Fitness: " + str(math.floor(p.best_fitness*100)) + "%" )
		app.generation.set("Generation: " + str(p.generation))
				
		p.show_pop()
		time.sleep(0.2)
	win.mainloop()


if __name__ == "__main__":
	main()