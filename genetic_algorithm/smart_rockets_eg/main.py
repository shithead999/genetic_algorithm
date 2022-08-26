from tkinter import Canvas, Tk
from settings import *
from rocket import Rocket
import math


class Main:
	def __init__(self, win):
		self.win  = win
		self.win.resizable(0,0)
		self.c = Canvas(self.win, bg="#F9F6EE", bd=0, highlightthickness=0, width=WIDTH, height=HEIGHT)
		self.c.pack(fill="both", expand=True)
		self.g_index = 0
		self.a = [Rocket(self.c) for i in range(100)]

	# this is the loop of the program
	def start(self):
		# update canvas for animation
		self.c.update()

		# apply forces (genes) to agents while all are not applied
		if self.g_index < FORCE_COUNT:
			for i in self.a:
				i.update(self.g_index)
			self.g_index += 1

		# sleep time to control FPS
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