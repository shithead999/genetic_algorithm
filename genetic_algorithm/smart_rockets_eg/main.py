from tkinter import Canvas, Tk
from settings import *
from rocket import Rocket
import math


class Main:
	def __init__(self, win):
		self.win  = win
		self.win.resizable(0,0)
		self.c = Canvas(self.win, bg="white", bd=0, highlightthickness=0, width=WIDTH, height=HEIGHT)
		self.c.pack(fill="both", expand=True)
		
		self.a = [Rocket(self.c) for i in range(50)]

	def start(self):
		self.c.update()
		for i in self.a:
			i.update()
		self.win.after(TIME_DELAY, self.start)


def main():
	win = Tk()
	obj = Main(win)
	obj.start()
	win.mainloop()

if __name__ == "__main__":
	main()