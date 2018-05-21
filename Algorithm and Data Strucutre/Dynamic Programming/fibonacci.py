'''
Implementation of Fibonacci Serires
'''

'''
def fibo(n, f):
	f[1] = 1
	
	for i in range(2, n+1):
		f[i] = f[i-1] + f[i-2]
	return f


def main():
	n = int(input('Enter nth term number: '))
	f = [0] * (n+1)
	print('Fibonacci series upto ', n,'term is ', fibo(n, f))


if __name__ == "__main__":
	main()
'''

# Memoized version of nth Fibonacci number

def fibo_memoized(n, lookup):
	if n == 0 or n == 1:
		lookup[n] = 1
	
	if lookup[n] is None:
		lookup[n] = fibo_memoized(n-1, lookup) + fibo_memoized(n-2, lookup)
	
	return lookup[n]


def main():
	n = int(input('Enter nth term number: '))
	lookup = [None] * (n+1)
	print('Fibonacci series upto ', n, 'term is ', fibo_memoized(n, lookup))

if __name__ == "__main__":
	main()
