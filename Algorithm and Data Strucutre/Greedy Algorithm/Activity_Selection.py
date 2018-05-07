'''
Implementation of Activity Selection problem
'''

def activitySelection(a):
	n = len(a)
	print('The following activities are selected: ')
	
	i = 0
	print(a[i], end='') # The first activity from sorted array is always selected
	for j in range(n):
		if a[j][0] >= a[i][1]:
			print(', ', a[j], end='')
			i = j
	print('\n')	

s = [int(x) for x in input('Enter start time of activities: ').split(',')]
f = [int(x) for x in input('Enter finish time of activities: ').split(',')]

tt = [[s, f] for s, f in zip(s, f)]
print('\nActivities are: ', tt)
tt_sort = sorted(tt, key=lambda x: x[1])

activitySelection(tt_sort)


