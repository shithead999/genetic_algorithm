from DNA import DNA
from population import Population
import time
from tkinter import Tk, StringVar, IntVar
from ui import App, StartApp
import math

start = Tk()
startapp = StartApp(start)
start.mainloop()

phrase = "Hello, World" if startapp.phrase.get().strip() == "" else startapp.phrase.get()
pop_size = 1000 if startapp.popsize.get() == 0 else startapp.popsize.get()
mutation_rate = 0.01 if startapp.mutation_rate.get().strip() == "" else float(startapp.mutation_rate.get())
timerun = "0.20" if startapp.timerun.get().strip()== ""else float(startapp.timerun.get())

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
		time.sleep(timerun)
		p.show_pop()
	win.mainloop()


if __name__ == "__main__":
	main()
