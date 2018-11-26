import numpy as np
import random

if __name__ == '__main__':
	n = [10000, 100000, 1000000]

	for i in n:
		name = 'data/file_{}.txt'.format(i)
		print 'Generating {}'.format(name)
		
		random_numbers = np.random.randint(low=-999, high=1000, size=i)

		np.savetxt(name, random_numbers, newline=' ',fmt="%d")