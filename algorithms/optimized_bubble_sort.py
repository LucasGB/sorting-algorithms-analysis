class OptimizedBubbleSort(object):
	"""docstring for OptimizedBubbleSort"""
	def __init__(self, array):
		super(OptimizedBubbleSort, self).__init__()
		self.array = array
		self.n_inst = 0
	
	def run(self):
		print 'Executing optimized bubble sort for ' + str(len(self.array)) + ' elements'

		if(len(self.array) <= 1):
			return self.array

		n = len(self.array) - 1
		for i in range(0, len(self.array)):
			for j in range(0, n):
				self.n_inst += 1
				
				if(self.array[j] > self.array[j+1]):
					aux = self.array[j+1]
					self.array[j+1] = self.array[j]
					self.array[j] = aux
			n -= 1

		return self.n_inst