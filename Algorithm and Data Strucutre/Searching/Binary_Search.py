'''
The following code implement Binary Search
'''

def binarySearchIterative(data, l, r, x):
	while l <= r:
		mid = (l+r)//2
		if data[mid] == x:
			return mid
		elif data[mid] < x:
			l = mid + 1
		else:
			r = mid - 1
	return -1

def binarySearchRecursive(data, l, r, x):
	if r >= l:
		mid = l + (r - l)//2
		
		if data[mid] == x:
			return mid
		elif data[mid] > x:
			return binarySearchRecursive(data, l, mid-1, x)
		else:
			return binarySearchRecursive(data, mid+1, r, x)
	else:
		return -1


data = [1, 2, 3, 4, 5, 6, 7, 8, 9]
x = 4

result_iter = binarySearchIterative(data, 0, len(data)-1, x)
result_rec = binarySearchRecursive(data, 0, len(data)-1, x)

if result_iter != -1:
	print('Element is present at index %d' % result_iter)
else:
	print('Element not found')


if result_rec != -1:
	print('Element is present at index %d' % result_rec)
else:
	print('Element not found')
