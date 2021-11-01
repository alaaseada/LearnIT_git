class Cart:
	def __init__(self, items):
		self.items = items

	def addItem(self, item):
		self.items.append(item)

	def deleteItem(self, item):
		self.items.remove(item)

