from algorithms.bubble_sort import BubbleSort
from algorithms.optimized_bubble_sort import OptimizedBubbleSort
from algorithms.insertion_sort import InsertionSort
from algorithms.selection_sort import SelectionSort
from algorithms.merge_sort import MergeSort
from algorithms.heap_sort import HeapSort
from algorithms.quick_sort import QuickSort
from algorithms.binary_search import BinarySearch
from algorithms.maximum_subarray import MaximumSubarray

from time import time

functions = [BubbleSort, OptimizedBubbleSort, InsertionSort, SelectionSort, MergeSort, HeapSort, QuickSort, MaximumSubarray]
n = [1000, 10000, 100000]

if __name__ == '__main__':

	for e in n:
		with open('data/file_' + str(e) + '.txt', 'r') as input_file:
			data = input_file.read()
			array = [int(i) for i in data.split()]

			for function in functions:
				with open('results/'+ str(function).split('.')[2][:-2] + '_' + str(e) + '.txt', 'w') as file:
					start_time = time()
					n_inst = function(array[:]).run()
					end_time = time() - start_time
					file.write('{} {}'.format(end_time, n_inst))
			
			with open('results/BinarySearch_' + str(e) + '.txt', 'w') as file:
				sorted_array = MergeSort(array[:]).run()
				start_time = time()
				n_inst = BinarySearch(array[:]).run(1)
				end_time = time() - start_time
				file.write('{} {}'.format(end_time, n_inst))