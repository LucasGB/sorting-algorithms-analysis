class MergeSort(object):
	"""docstring for MergeSort"""
	def __init__(self, array):
		super(MergeSort, self).__init__()
		self.array = array
		self.n_inst = 0
	
	def merge(self, arr, l, m, r):

		self.n_inst += 1

		n1 = m - l + 1
		n2 = r - m
		L = [0] * (n1)
		R = [0] * (n2)

		for i in range(0 , n1):
			L[i] = arr[l + i]

		for j in range(0 , n2):
			R[j] = arr[m + 1 + j]

		i = 0
		j = 0
		k = l

		while i < n1 and j < n2:
			if L[i] <= R[j]:
				arr[k] = L[i]
				i += 1
			else:
				arr[k] = R[j]
				j += 1
			k += 1

		while i < n1:
			arr[k] = L[i]
			i += 1
			k += 1
		while j < n2:
			arr[k] = R[j]
			j += 1
			k += 1

	def mergesort(self, arr, l, r):
		self.n_inst += 1

		if l < r:
			m = (l+(r-1))/2

			self.mergesort(arr, l, m)
			self.mergesort(arr, m+1, r)
			self.merge(arr, l, m, r)

		return arr
	def run(self):
		print 'Executing Merge Sort for ' + str(len(self.array)) + ' elements'
		self.mergesort(self.array[:], 0, len(self.array[:]) - 1)

		return self.n_inst