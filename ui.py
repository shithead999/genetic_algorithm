from tkinter import *

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

		self.mainF = Frame(self.root)
		self.bplabel = Label(self.mainF, textvariable=self.best_phrase, padx=20, pady=20, font=("monospace", 20, "bold"))
		self.bplabel.pack(side=TOP, fill=X)

		self.bottomF = Frame(self.mainF)

		self.blFrame = Frame(self.bottomF)

		self.bll1 = Label(self.blFrame, anchor="w", justify="left", textvariable=self.best_fit, padx=2, pady=2, font=("monospace", 15))
		self.bll1.pack(fill=X)
		self.bll3 = Label(self.blFrame, anchor="w", justify="left", textvariable=self.generation, padx=2, pady=2, font=("monospace", 15))
		self.bll3.pack(fill=X)

		self.blFrame.pack(side=LEFT, padx = 20, pady = 20, fill=BOTH)
		
		self.brFrame = Frame(self.bottomF)
		
		self.brf1 = Label(self.brFrame, textvariable=self.l1, padx=2, pady=2, font=("monospace", 15))
		self.brf1.pack()
		self.brf2 = Label(self.brFrame, textvariable=self.l2, padx=2, pady=2, font=("monospace", 15))
		self.brf2.pack()
		self.brf3 = Label(self.brFrame, textvariable=self.l3, padx=2, pady=2, font=("monospace", 15))
		self.brf3.pack()
		self.brf4 = Label(self.brFrame, textvariable=self.l4, padx=2, pady=2, font=("monospace", 15))
		self.brf4.pack()
		self.brf5 = Label(self.brFrame, textvariable=self.l5, padx=2, pady=2, font=("monospace", 15))
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
		self.draw_ui()

	def draw_ui(self):
		f1 = Frame(self.root)
		Label(f1, anchor="w", justify="left", text="Phrase: ", font = ("monospace", 10)).pack(side=LEFT, fill=BOTH)
		e = Entry(f1, textvariable=self.phrase, font = ("monospace", 10))
		e.pack(side = RIGHT)
		f1.pack(fill=X, padx = 10, pady = 10)
		f2 = Frame(self.root)
		Label(f2, text="Mutation Rate: ", font = ("monospace", 10)).pack(side=LEFT, fill=BOTH)
		e1 = Entry(f2, textvariable=self.mutation_rate, font = ("monospace", 10))
		e1.pack(side = RIGHT, fill=X)
		f2.pack(fill=X, padx = 10, pady = 10)
		f3 = Frame(self.root)
		Label(f3, text="Population Size: ", font = ("monospace", 10)).pack(side=LEFT, fill=BOTH)
		e2 = Entry(f3, textvariable=self.popsize, font = ("monospace", 10))
		e2.pack(side = RIGHT, fill=X)
		f3.pack(fill=X, padx = 10, pady = 10)
		b = Button(self.root, text="Start", command=self.root.destroy)
		b.pack()