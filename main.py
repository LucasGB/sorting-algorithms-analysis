from algorithms.bubble_sort import BubbleSort
from algorithms.optimized_bubble_sort import OptimizedBubbleSort
from algorithms.insertion_sort import InsertionSort
from algorithms.selection_sort import SelectionSort
from algorithms.merge_sort import MergeSort
from algorithms.heap_sort import HeapSort
from algorithms.quick_sort import QuickSort


if __name__ == '__main__':
	with open('data/file_10000.txt', 'r') as file:
		data = file.read()
		array = [int(i) for i in data.split()]
		
		#bubble_sort = BubbleSort(array)
		#print bubble_sort.run()
		
		#optimized_bubble_sort = OptimizedBubbleSort(array)
		#print optimized_bubble_sort.run()

		#insertion_sort = InsertionSort(array)
		#print insertion_sort.run()

		#selection_sort = SelectionSort(array)
		#print selection_sort.run()

		#merge_sort = MergeSort(array)
		#print merge_sort.run(array, 0, len(array) - 1)

		#heap_sort = HeapSort(array)
		#print heap_sort.run(array)

		quick_sort = QuickSort(array)
		quick_sort.run(array)