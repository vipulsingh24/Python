'''
Implementation of Merge Sort
'''

def merge(a, l, m, r):
	n1 = m - l + 1
	n2 = r - m
	
	# Create temp arrays
	L = [0] * n1
	R = [0] * n2

	# Copy data to temp arrays L[] and R[]
	for i in range(0, n1):
		L[i] = a[l+i]

	for i in range(0, n2):
		R[i] = a[m+1+i]

	# Merge the temp array back into array
	i = 0; j = 0; k = l
	
	while i < n1 and j < n2:
		if L[i] <= R[j]:
			a[k] = L[i]
			i += 1
		else:
			a[k] = R[j]
			j += 1
		k += 1

	# Copy the remaining element if any
	while i < n1:
		a[k] = L[i]
		i += 1
		k += 1

	while j < n2:
		a[k] = R[j]
		j += 1
		k += 1

def mergeSort(a, l, r):
	if l < r:
		m = (l + r)//2

		# Sort first and second halfs
		mergeSort(a, l, m)
		mergeSort(a, m+1, r)
		merge(a, l, m, r)


# a = [6, 9, 2, 5, 10, 8, 1, 4, 7, 3]
a = [int(x) for x in input('Enter number:').split()]
n = len(a)

print('Array before Merge Sort: ', a)

mergeSort(a, 0, n-1)

print('Array after Merge Sort: ', a)
