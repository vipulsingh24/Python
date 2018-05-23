'''
Implementation of Longest Increasing Subsequence Problem
'''

def lis(a):
	n = len(a)
	lis = [1] * n

	for i in range(1, n):	
		for j in range(0, i):
			if a[i] > a[j] and lis[i] < lis[j] + 1:
				lis[i] = lis[j] + 1

	return max(lis)


a = [10, 22, 9, 33, 21, 50, 41, 60]
n = len(a)
print('Length of LIS is ', lis(a))

