l = []
for i in range(10):
	l.append([f'{(n+1) + (i*10):4}' for n in range(10)])

l = reversed([reversed(row) if i%2 else row for i, row in enumerate(l)])

for row in l:
    print(' | '.join(row))
