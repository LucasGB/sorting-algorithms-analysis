import numpy as np
from algorithms.bubble_sort import BubbleSort


if __name__ == '__main__':
	with open('data/file_10000.txt', 'r') as file:
		array = np.loadtxt('data/file_10000.txt', dtype=np.dtype(int), delimiter=',', unpack=False)
		print array
		#b = BubbleSort(array)
		#b.run()