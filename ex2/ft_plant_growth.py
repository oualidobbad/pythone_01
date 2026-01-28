class Plant:
	def __init__(self, name, height, agePlanet, growPlanet):
		self.name = name
		self.height = height
		self.agePlanet = agePlanet
		self.growPlanet = growPlanet

	def grow(self):
		self.growPlanet += self.growPlanet
	def age(self):
		self.agePlanet += 1
		self.grow()
	def get_info(self):
		return f"{self.name}: {self.height}cm, {self.age} days"


if __name__ == "__main__":
	p = Plant("Rose", 25, 30)
	p1 = Plant("Sunflower", 80, 45)
	p2 = Plant("Rose", 15, 120)
	
	
	print("=== Garden Plant Registry ===")
	p.display()
	p1.display()
	p2.display()