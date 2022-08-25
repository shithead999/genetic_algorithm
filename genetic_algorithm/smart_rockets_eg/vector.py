import math

class Vector:
	def __init__(self, x=1, y=1):
		self.x = x
		self.y = y

	def get_mag(self):
		return math.sqrt(self.x**2 + self.y**2)

	def normalize(self):
		self.x /= self.get_mag()
		self.y /= self.get_mag()

	def get_angle(self):
		return math.floor(math.atan2(self.y, self.x))

	def add(self, v):
		if isinstance(v, Vector):
			self.x += v.x
			self.y += v.y
		else:
			self.x += v
			self.y += v		

	def mult(self, v):
		if isinstance(v, Vector):
			self.x *= v.x
			self.y *= v.y
		else:
			self.x *= v
			self.y *= v

	def __str__(self):
		return f"[X={self.x} Y={self.y}]"

	@staticmethod
	def from_angle(angle):
		return Vector(math.cos(angle), math.sin(angle))	

	@staticmethod
	def get_angle_between(v1, v2):
		n = v1.x*v2.x + v1.y*v2.y
		d = v1.get_mag()*v2.get_mag()
		return math.acos(n/d)