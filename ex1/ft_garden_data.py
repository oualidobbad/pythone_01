class Plant:
	def __init__(self, name, height, age):
		self.name = name
		self.height = height
		self.age = age
	def display(self):
		print(f"{self.name}: {self.height}cm, {self.age} days")

if __name__ == "__main__":
	p = Plant("Rose", 25, 30)
	p1 = Plant("Sunflower", 80, 45)
	p2 = Plant("Rose", 15, 120)

	print("=== Garden Plant Registry ===")
	p.display()
	p1.display()
	p2.display()
