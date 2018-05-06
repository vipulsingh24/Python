'''
Implemetation of Interpolation Search using Probe positio formula,
pos = low + [ (x-arr[low])*(high-low) / (arr[high]-arr[low]) ]
'''

def interpolationSearch(a, n, x):
	low = 0
	high = n - 1
	
	while low <= high and x >= a[low] and x <= a[high]:
		# Probe position formula
		pos = int(low + ( (x - a[low]) * (high - low) / (a[high] - a[low]) ))
		
		if a[pos] == x:
			return pos
		
		if a[pos] < x:
			low = pos + 1;
		else:
			high = pos - 1;

	return -1


# Array to be sorted
#a = [1, 2, 3, 4, 5]

a = [int(x) for x in input('Enter element: ').split(',')]
n = len(a)

#x = 3
x = int(input('Enter element to be search: '))
index = interpolationSearch(a, n, x)

if index != -1:
	print('Element found at index', index)
else:
	print('Element not found')


