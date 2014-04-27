## Python Question???

def proc1(p):
	p[0] = p[1]

def proc2(p):
	#p = p + [1]
	p += [1]

p = [1,2,3]
print p
proc1(p)
print p

