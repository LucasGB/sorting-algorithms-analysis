class SelectionSort(object):
	"""docstring for SelectionSort"""
	def __init__(self, array):
		super(SelectionSort, self).__init__()
		self.array = array
		self.n_inst = 0

	def run(self):
		print 'Executing selection sort for ' + str(len(self.array)) + ' elements'
		
		for i in range(len(self.array) - 1, 0, -1):
			max_num_pos = 0
			
			for j in range(1, i + 1):
				self.n_inst += 1

				if self.array[j] > self.array[max_num_pos]:
					max_num_pos = j

			temp = self.array[i]
			self.array[i] = self.array[max_num_pos]
			self.array[max_num_pos] = temp

		return self.n_inst