'''
Implementation of Heap Sort
'''

def heapify(a, n, i):
	largest = i
	l = 2 * i + 1	# Left child
	r = 2 * i + 2	# Right child

	if l < n and a[i] < a[l]:
		largest = l
	if r < n and a[largest] < a[r]:
		largest = r

	if largest != i:
		a[i], a[largest] = a[largest], a[i]
		heapify(a, n, largest)


def heapSort(a):
	n = len(a)
	
	for i in range(n, -1, -1):
		heapify(a, n, i)

	# extract elements one by one
	for i in range(n-1, 0, -1):
		a[i], a[0] =  a[0], a[i]
		heapify(a, i, 0)


# a = [4, 8, 9, 1, 7, 2, 10, 3, 6, 5]

a = [int(x.strip()) for x in input('Enter elements: ').split(',')]

print('Elements before sort: ', a)
heapSort(a)
n = len(a)
print('Elements after sort: ', a)
