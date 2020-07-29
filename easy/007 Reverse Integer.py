import time
class Solution:
	def reverse(self, x: int) -> int:
		start_time = time.time()

		if x > 0:
			string = str(x)[::-1]
			x = int(string)
		else:
			string = str(abs(x))[::-1]
			x = -(int(string))

		neg_limit = - 0x80000000
		pos_limit = 0x7fffffff

		if (x < 0):
			val = x & neg_limit
			if (val == neg_limit):
				print(f'total time: {time.time() - start_time}')
				return x
			else:
				print(f'total time: {time.time() - start_time}')
				return 0
		elif (x == 0):
			print(f'total time: {time.time() - start_time}')
			return x
		else:
			val = x & pos_limit
			if (val == x):
				print(f'total time: {time.time() - start_time}')
				return x
			else:
				print(f'total time: {time.time() - start_time}')
				return 0

	def reverse2(self, x: int) -> int:
		start_time = time.time()
		res, remaining = 0, abs(x)
		while remaining:
			res = res * 10 + remaining % 10
			remaining //= 10
		if not (-(2 ** 31) <= res <= (2 ** 31 - 1)):
			print(f'total time: {time.time() - start_time}')
			return 0
		else:
			print(f'total time: {time.time() - start_time}')
			return res if x > 0 else - res

	def reverse3(self, x: int) -> int:
		start_time = time.time()
		neg = False
		if x < 0:
			neg = True
			x *= -1
		res = 0
		while x > 0:
			res = res * 10 + x % 10
			x = x // 10
		if res > 2 ** 31:
			print(f'total time: {time.time() - start_time}')
			return 0
		if neg:
			print(f'total time: {time.time() - start_time}')
			return -res
		print(f'total time: {time.time() - start_time}')
		return res

	def reverse4(self, x: int) -> int:
		start_time = time.time()
		minus_fg = True if (x < 0) else False
		str_x = str(-x) if (minus_fg) else str(x)
		reversed_str_x = str_x[::-1]
		zero_removed = int(reversed_str_x)
		ans = -zero_removed if minus_fg else zero_removed
		print(f'total time: {time.time() - start_time}')
		return ans if (ans >= -pow(2, 31) and ans <= pow(2, 31)) else 0


number = Solution()
print(number.reverse(123456789))
print(number.reverse2(123456789))
print(number.reverse3(123456789))
print(number.reverse4(1234567890))
