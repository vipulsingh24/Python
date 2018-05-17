'''
Implementation of Minimum number of coins
needed to make a change
'''

def findMin(n):
	result = []
	for i in range(len(change)-1, -1, -1):
		while(n >= change[i]):
			n -= change[i]
			result.append(change[i])
	
	return result


change = [1, 2, 5, 10, 20, 50, 100, 200, 500, 2000]

n = int(input('Enter value: '))
print('Following is minimal number of change for ', n, 'is ', findMin(n))
