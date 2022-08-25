from tkinter import *
from customtkinter import *

class App:
	def __init__(self, root):
		self.root = root
		self.best_phrase = StringVar()
		self.l1 = StringVar()
		self.l2 = StringVar()
		self.l3 = StringVar()
		self.l4 = StringVar()
		self.l5 = StringVar()
		self.generation = StringVar()
		self.best_fit = StringVar()
		self.phrase = StringVar()
		self.best_phrase.set("Hello, World")
		self.draw_ui()

	def draw_ui(self):	

		self.mainF = CTkFrame(self.root)
		self.bplabel = CTkLabel(self.mainF, textvariable=self.best_phrase, padx=20, pady=20)
		self.bplabel.pack(side=TOP, fill=X)

		self.bottomF = CTkFrame(self.mainF)

		self.blFrame = CTkFrame(self.bottomF)

		self.bll1 = CTkLabel(self.blFrame, anchor="w", justify="left", textvariable=self.best_fit, padx=2, pady=2)
		self.bll1.pack(fill=X)
		self.bll3 = CTkLabel(self.blFrame, anchor="w", justify="left", textvariable=self.generation, padx=2, pady=2)
		self.bll3.pack(fill=X)

		self.blFrame.pack(side=LEFT, padx = 20, pady = 20, fill=BOTH)
		
		self.brFrame = CTkFrame(self.bottomF)
		
		self.brf1 = CTkLabel(self.brFrame, textvariable=self.l1, padx=2, pady=2)
		self.brf1.pack()
		self.brf2 = CTkLabel(self.brFrame, textvariable=self.l2, padx=2, pady=2)
		self.brf2.pack()
		self.brf3 = CTkLabel(self.brFrame, textvariable=self.l3, padx=2, pady=2)
		self.brf3.pack()
		self.brf4 = CTkLabel(self.brFrame, textvariable=self.l4, padx=2, pady=2)
		self.brf4.pack()
		self.brf5 = CTkLabel(self.brFrame, textvariable=self.l5, padx=2, pady=2)
		self.brf5.pack()


		self.brFrame.pack(side=RIGHT, fill=BOTH, padx=20, pady=20)
		self.bottomF.pack(side=BOTTOM)

		self.mainF.pack()

class StartApp:
	def __init__(self, root):
		self.root = root
		self.phrase = StringVar()
		self.mutation_rate = StringVar()
		self.popsize = IntVar()
		self.timerun=StringVar()
		self.draw_ui()

	def draw_ui(self):
		f1 = CTkFrame(self.root)
		CTkLabel(f1, anchor="w", justify="left", text="Phrase: ", text_font=("ubuntu", 15)).pack(side=LEFT, fill=BOTH)
		e = CTkEntry(f1, textvariable=self.phrase, text_font=("", 15))
		e.pack(side = RIGHT)
		f1.pack(fill=X, padx = 10, pady = 10)
		f2 = CTkFrame(self.root)
		CTkLabel(f2, anchor="w", justify="left", text="Mutation Rate: ", text_font=("ubuntu", 15)).pack(side=LEFT, fill=BOTH)
		e1 = CTkEntry(f2, textvariable=self.mutation_rate, text_font=("", 15))
		e1.pack(side = RIGHT, fill=X)
		f2.pack(fill=X, padx = 10, pady = 10)
		f3 = CTkFrame(self.root)
		CTkLabel(f3, anchor="w", justify="left", text="Population Size: ", text_font=("ubuntu", 15)).pack(side=LEFT, fill=BOTH)
		e2 = CTkEntry(f3, textvariable=self.popsize, text_font=("", 15))
		e2.pack(side = RIGHT, fill=X)
		f3.pack(fill=X, padx = 10, pady = 10)
		f4 = CTkFrame(self.root)
		CTkLabel(f4, anchor="w", justify="left", text="Time Run: ", text_font=("ubuntu", 15)).pack(side=LEFT, fill=BOTH)
		e3 = CTkEntry(f4, textvariable=self.timerun, text_font=("", 15))
		e3.pack(side = RIGHT, fill=X)
		f4.pack(fill=X, padx = 10, pady = 10)
		b = CTkButton(self.root, text="Start", command=self.root.destroy)
		b.pack()
