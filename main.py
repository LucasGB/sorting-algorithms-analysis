from algorithms.bubble_sort import BubbleSort
from algorithms.optimized_bubble_sort import OptimizedBubbleSort


if __name__ == '__main__':
	with open('data/file_10000.txt', 'r') as file:
		data = file.read()
		array = [int(i) for i in data.split()]
		
		#bubble_sort = BubbleSort(array)
		#bubble_sort.run()
		
		#optimized_bubble_sort = OptimizedBubbleSort(array)
		#optimized_bubble_sort.run()