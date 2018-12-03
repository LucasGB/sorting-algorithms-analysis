class BinarySearch(object):
	"""docstring for BinarySearch"""
	def __init__(self, array):
		super(BinarySearch, self).__init__()
		self.array = array
	
	def run(self, item):
		print 'Executing Binary Search'

		first = 0
		last = len(self.array)-1

		while(first <= last):
			mid = (first + last) / 2
			if self.array[mid] == item :
				return mid
			else:
				if item < self.array[mid]:
					last = mid - 1
				else:
					first = mid + 1	
		return None