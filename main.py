from algorithms.bubble_sort import BubbleSort
from algorithms.optimized_bubble_sort import OptimizedBubbleSort
from algorithms.insertion_sort import InsertionSort
from algorithms.selection_sort import SelectionSort

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

		selection_sort = SelectionSort(array)
		print selection_sort.run()