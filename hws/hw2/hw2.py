def median(a, b, c):
    if a > b:
        if c >= a:
            return a
        elif c <= b:
            return b
        else:
            return c
    else:
        if c <= a:
            return a
        elif c >= b:
            return b
        else:
            return c


def find_last(s, t):
	last = -1
	pos = 0
	while True:
		pos = s.find(t, pos)
		if pos == -1:
			return last
		last = pos
		pos = pos + 1
	return last

# better solution
def find_last_ideal(s, t):
	last = -1
	while True:
		pos = s.find(t, last + 1)
		if pos == -1:
			return last
		last = pos


def print_multiplication_table(n):
	i = 1
	while i <= n:
		j = 1
		while j <= n:
			print str(i) + ' * ' + str(j) + ' = ' + str(i*j)
			j = j + 1
		i = i + 1


### Test Case
#print(median(1,2,3))

#print find_last('aaaa', 'a')
#print find_last_ideal('aaaa', 'a')

print_multiplication_table(2)

