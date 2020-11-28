def shapeArea(n):
	total = 1
	for i in range(1, n+1):
		total = total + (i-1)*4
	return total

def shape(n):
	return n**2+(n-1)**2



print(shapeArea(4))
print(shape(4))
