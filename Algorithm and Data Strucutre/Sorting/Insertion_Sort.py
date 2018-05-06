'''
Implementation of Insertion Sort
'''

def insertionSort(a):
	for i in range(1, len(a)):
		key = a[i]
		j = i - 1
		while j >= 0 and key < a[j]:
			a[j+1], a[j] = a[j], a[j+1]
			j -= 1
		a[j+1] = key


a = [int(x) for x in input('Enter elements: ').split()]

insertionSort(a)

print('After Insertion Sort: ', a)






