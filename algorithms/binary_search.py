class BinarySearch(object):
	"""docstring for BinarySearch"""
	def __init__(self, array):
		super(BinarySearch, self).__init__()
		self.array = array
		self.n_inst = 0
	
	def run(self, item):
		print 'Executing Binary Search for ' + str(len(self.array)) + ' elements'

		first = 0
		last = len(self.array)-1

		while(first <= last):
			self.n_inst += 1

			mid = (first + last) / 2
			if self.array[mid] == item :
				return self.n_inst, mid
			else:
				if item < self.array[mid]:
					last = mid - 1
				else:
					first = mid + 1	
		return self.n_inst, None