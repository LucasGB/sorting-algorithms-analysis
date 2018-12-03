import numpy as np
import random

if __name__ == '__main__':
	n = [1000, 10000, 100000]

	for i in n:
		name = 'data/file_{}.txt'.format(i)
		print 'Generating {}'.format(name)
		
		random_numbers = np.random.randint(low=(i - 1) * -1, high=i, size=i)

		np.savetxt(name, random_numbers, newline=' ',fmt="%d")