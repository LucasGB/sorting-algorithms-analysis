class BubbleSort(object):
	"""docstring for BubbleSort"""
	def __init__(self, array):
		super(BubbleSort, self).__init__()
		self.array = array
	
	def run(self):
		print 'Executing bubble sort'

		if(len(self.array) <= 1):
			return self.array

		for i in range(0, len(self.array)):
			for j in range(0, len(self.array)-1):
				if(self.array[j] > self.array[j+1]):
					aux = self.array[j+1]
					self.array[j+1] = self.array[j]
					self.array[j] = aux

		print self.array