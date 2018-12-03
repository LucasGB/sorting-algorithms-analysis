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

if __name__ == '__main__':
	with open('data/file_10000.txt', 'r') as file:
		data = file.read()
		array = [int(i) for i in data.split()]
		
		#bubble_sort = BubbleSort(array[:])
		#print bubble_sort.run()
		
		#optimized_bubble_sort = OptimizedBubbleSort(array[:])
		#print optimized_bubble_sort.run()

		#insertion_sort = InsertionSort(array[:])
		#print insertion_sort.run()

		#selection_sort = SelectionSort(array[:])
		#print selection_sort.run()

		#merge_sort = MergeSort(array[:])
		#print merge_sort.run(array[:], 0, len(array[:]) - 1)

		#heap_sort = HeapSort(array[:])
		#print heap_sort.run(array[:])

		start_time = time()
		quick_sort = QuickSort(array[:])
		sorted_arr = quick_sort.run()

		binary_search = BinarySearch(sorted_arr)
		print binary_search.run(1)

		maximum_subarray = MaximumSubarray(array)
		print maximum_subarray.run()
		end_time = time() - start_time

		print 'Tempo de execução: %0.3f segundos' % end_time