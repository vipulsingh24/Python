'''
Implementation of Quick Sort
Here, pivot is the last element
'''
import re

def partition(a, low, high):
	i = low - 1
	pivot = a[high]

	for j in range(low, high):
		if a[j] <= pivot:
			i += 1
			a[i], a[j] = a[j], a[i]
	a[i+1], a[high] = a[high], a[i+1]
	return (i+1)

def quickSort(a, low, high):
	if low < high:
		# Partitioning index
		pi = partition(a, low, high)
		quickSort(a, low, pi -1)
		quickSort(a, pi+1, high)

a = [int(x) for x in input('Enter element: ').split()]
n = len(a)

print('Element before sort: ', a)
quickSort(a, 0, n-1)
print('Element after sort: ', a)
