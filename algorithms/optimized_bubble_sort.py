class OptimizedBubbleSort(object):
	"""docstring for OptimizedBubbleSort"""
	def __init__(self, array):
		super(OptimizedBubbleSort, self).__init__()
		self.array = array
	
	def run(self):
		print 'Executing optimized bubble sort'

		if(len(self.array) <= 1):
			return self.array

		n = len(self.array) - 1
		for i in range(0, len(self.array)):
			for j in range(0, n):
				if(self.array[j] > self.array[j+1]):
					aux = self.array[j+1]
					self.array[j+1] = self.array[j]
					self.array[j] = aux
			n -= 1

		print self.array