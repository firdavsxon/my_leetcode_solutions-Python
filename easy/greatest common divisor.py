def gcd(lst, num):
	result=lst[0]
	for i in lst[1:]:
		result = helper(result, i)
	return result

def helper(a,b):
	while b>0:
		a, b = b, a%b
	return a

print(gcd([2, 4 ,6 ,8 ,10], 5))
print(gcd([1,3,5,7], 5))