'''
Implementation of Minimum Platform required 
for a Railway/Bus Station
'''




arr = [900, 940, 950, 1100, 1500, 1800]
dep = [910, 1200, 1120, 1130, 1900, 2000]

n = len(arr)

print('Minimum Number of Platforms Required = ', findPlatform(arr, dep, n))

