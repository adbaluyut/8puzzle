class Node:
	def __init__(self, data=None, parent=None, depth=0, weight=0):
		self.data = data
		self.parent = parent
		self.depth = depth
		self.weight = weight


	def findEmpty(self):
		for i in range(len(self.data)):
			if self.data[i] == 0:
				return i


	def up(self, index):
		arr = list(self.data)
		if index > 2:
			arr[index], arr[index-3] = arr[index-3], arr[index]
			return Node(data=arr, parent=self)
		else:
			return None


	def down(self, index):
		arr = list(self.data)
		if index < 6:
			arr[index], arr[index+3] = arr[index+3], arr[index]
			return Node(data=arr, parent=self)
		else:
			return None


	def left(self, index):
		arr = list(self.data)
		if index % 3 != 0:
			arr[index], arr[index-1] = arr[index-1], arr[index]
			return Node(data=arr, parent=self)
		else:
			return None


	def right(self, index):
		arr = list(self.data)
		if (index + 1) % 3 != 0:
			arr[index], arr[index+1] = arr[index+1], arr[index]
			return Node(data=arr, parent=self)
		else:
			return None


	def checkMoves(self):
		index = self.findEmpty()
		neighbors = []
		neighbors.append(self.up(index))
		neighbors.append(self.down(index))
		neighbors.append(self.left(index))
		neighbors.append(self.right(index))
		
		return [i for i in neighbors if i]