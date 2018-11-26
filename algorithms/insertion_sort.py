class InsertionSort(object):
	"""docstring for InsertionSort"""
	def __init__(self, array):
		super(InsertionSort, self).__init__()
		self.array = array

	def run(self):
		print 'Executing insertion sort'
		
		for i in range(1, len(self.array)):
			currentvalue = self.array[i]
			position = i
			
			while position > 0 and self.array[position - 1] > currentvalue:
				self.array[position] = self.array[position - 1]
				position -= 1

			self.array[position] = currentvalue

		return self.array