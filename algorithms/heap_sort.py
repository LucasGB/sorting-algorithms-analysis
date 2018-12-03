class HeapSort(object):
	"""docstring for HeapSort"""
	def __init__(self, array):
		super(HeapSort, self).__init__()
		self.array = array
		self.n_inst = 0
	
	def run(self):
		print 'Executing Heap Sort for ' + str(len(self.array)) + ' elements'
		n = len(self.array) 

		for i in range(n, -1, -1): 
			self.n_inst += 1
			self.heapify(self.array, n, i) 

		for i in range(n-1, 0, -1): 
			self.n_inst += 1
			self.array[i], self.array[0] = self.array[0], self.array[i]
			self.heapify(self.array, i, 0)

		return self.n_inst

	def heapify(self, arr, n, i): 
		largest = i
		l = 2 * i + 1
		r = 2 * i + 2

		if l < n and arr[i] < arr[l]: 
			largest = l 

		if r < n and arr[largest] < arr[r]: 
			largest = r 

		if largest != i: 
			arr[i],arr[largest] = arr[largest],arr[i] # swap 

			self.heapify(arr, n, largest) 