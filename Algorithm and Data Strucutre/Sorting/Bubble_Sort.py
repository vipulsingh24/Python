'''
Implementation of Bubble Sort
'''

def bubbleSort(a):
	n = len(a)
	
	for i in range(n):
		swapped = False
		for j in range(0, n-i-1):
			if a[j] > a[j+1]:
				a[j], a[j+1] = a[j+1], a[j]
				swapped = True

		# If no two elements were swapped by innere loop then break
		if swapped == False:
			break

a = [int(x) for x in input('Enter unsorted array: ').split()]

bubbleSort(a)

print('Sorted array: ', a)

