class QuickSort(object):
	"""docstring for QuickSort"""
	def __init__(self, array):
		super(QuickSort, self).__init__()
		self.array = array
	
	def run(self, arr):
		print 'Executing quick sort'
		
		self.quickSortHelper(arr, 0, len(self.array) - 1)

		return arr

	def quickSortHelper(self, array, first, last):
		if first < last:
			splitpoint = self.partition(array, first, last)

			self.quickSortHelper(array, first, splitpoint - 1)
			self.quickSortHelper(array, splitpoint + 1, last)

	def partition(self, array, first, last):
		pivotvalue = array[first]

		leftmark = first+1
		rightmark = last
		done = False

		while not done:
			while leftmark <= rightmark and array[leftmark] <= pivotvalue:
				leftmark = leftmark + 1

			while array[rightmark] >= pivotvalue and rightmark >= leftmark:
				rightmark = rightmark -1

			if rightmark < leftmark:
				done = True
			else:
				temp = array[leftmark]
				array[leftmark] = array[rightmark]
				array[rightmark] = temp

		temp = array[first]
		array[first] = array[rightmark]
		array[rightmark] = temp

		return rightmark