class CrazyClass():
	def unimportant_thing(self, x, y, z):
		for i in range(x, y):
			z()

	def critical_method(self):
		super_critical_thing()

	def more_random_stuff(self, a, b, c):
		return a(b(c()))