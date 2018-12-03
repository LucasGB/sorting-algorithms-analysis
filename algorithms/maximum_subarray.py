class MaximumSubarray(object):
	"""docstring for MaximumSubarray"""
	def __init__(self, array):
		super(MaximumSubarray, self).__init__()
		self.array = array
	
	def run(self):
		print 'Executing Maximum Subarray Search for ' + str(len(self.array)) + ' elements'
		