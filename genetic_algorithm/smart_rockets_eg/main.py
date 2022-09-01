from tkinter import Canvas, Tk
from settings import *
import math
from population import Population
from pillars import Pillar

class Main:
	def __init__(self, win):
		self.win  = win
		self.win.resizable(0,0)
		self.c = Canvas(self.win, bg=COLORS[3], bd=0, highlightthickness=0, width=WIDTH, height=HEIGHT)
		self.c.pack(fill="both", expand=True)

		self.target = self.c.create_rectangle(
			[TARGET_COOR[0]-TARGET_SIZE, TARGET_COOR[1]-TARGET_SIZE, TARGET_COOR[0]+TARGET_SIZE, TARGET_COOR[1]+TARGET_SIZE],
			fill=COLORS[0],
			outline=None,
			width=0,
		)

		self.pillars = [
			Pillar(self.c, WIDTH/2 - 200, HEIGHT*0.40, 400, 20),
			# Pillar(self.c, WIDTH/2 - 220, HEIGHT*0.30, 20, 200),
			Pillar(self.c, WIDTH/2 - 100, HEIGHT*0.50, 20, 200),
		]
		self.population = Population(self.c, self.pillars)

	def start(self):
		self.c.update()
		if self.population.g_index < FORCE_COUNT:
			self.population.update()
		else:
			# perform genetic algorithm to get new generation
			self.population.calc_fitness()
			self.population.natural_selection()
			self.population.generate()

		self.win.after(TIME_DELAY, self.start)


def main():
	win = Tk()
	win.title("Genetic Algorithm")
	win.resizable(0,0)
	obj = Main(win)
	obj.start()
	win.mainloop()

if __name__ == "__main__":
	main()
