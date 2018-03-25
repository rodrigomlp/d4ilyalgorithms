'''
Given a number x and positions i and j, swap positions i and j
Example:

1001 1000 with i = 0 and j = 4 we get:

1000 0001
'''
def swap(x, i, j):
	# find if bits are different
	if(x >> i) & 1 != (x >> j) & 1:
		bit_mask = (1 << i) | (1 << j)
		x^= bit_mask
	return x

