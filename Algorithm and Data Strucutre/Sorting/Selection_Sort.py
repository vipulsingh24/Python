'''
Implementation of Selection Sort
'''

#A = [2, 5, 1, 3, 7, 9, 4, 10, 8, 6]
a = [int(x) for x in input('Enter number:').split()]

for i in range(len(a)):
	min_index = i
	for j in range(i+ 1, len(a)):
		if a[min_index] > a[j]:
			min_index = j
	a[i], a[min_index] = a[min_index], a[i]
print('Sorted array: ')
for i in range (len(a)):
	print('%d'% a[i])
