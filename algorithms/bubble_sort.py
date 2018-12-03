class BubbleSort(object):
	"""docstring for BubbleSort"""
	def __init__(self, array):
		super(BubbleSort, self).__init__()
		self.array = array
		self.n_inst = 0
	
	def run(self):
		print 'Executing bubble sort for ' + str(len(self.array)) + ' elements'

		if(len(self.array) <= 1):
			return self.array

		for i in range(0, len(self.array)):
			for j in range(0, len(self.array)-1):
				self.n_inst += 1
				
				if(self.array[j] > self.array[j+1]):
					aux = self.array[j+1]
					self.array[j+1] = self.array[j]
					self.array[j] = aux

		return self.n_inst