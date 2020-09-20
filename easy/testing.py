def word_count_engine(document):
	if not document:
		return []

	d = {}

	for i in document:
		if i == '.' or i == '!' or i == ',' or i == "'":
			document = document.replace(i, '')

	# splitted_words = document.split(' ')
	splitted_words = []
	window_start = 0
	for window_end, char in enumerate(document):
		if char == ' ':
			splitted_words.append(document[window_start:window_end])
			window_start = window_end + 1
		if window_end == len(document) - 1:
			splitted_words.append(document[window_start:window_end + 1])
	for word in splitted_words:
		d[word.lower()] = d.get(word.lower(), 0) + 1

	sorted_list = sorted(([key, str(value)] for key, value in d.items()), key=lambda x: x[1], reverse=True)

	return sorted_list


#
# document = "Practice makes perfect. you'll onlyget Perfect by practice. just practice!"
# print(word_count_engine(document))
# print(word_count_engine("Practice makes perfect, you'll get perfecT by practice. just practice! just just just!!"))


# Another exercise
"""

input: s = 'ababcbacadefegdehijhklij'
output: lst = [9,7,8]

-----
input: s= 'abc' 
output: lst = [1,1,1]

-----
input: s= 'abca' 
output: lst = [4] 
explanation: because a appears in list more than once total will be 4

"""


def func(s):
	res = []
	starting_point = 0
	ending_point = 0
	max_length = 0
	between_letters = {}
	while starting_point < len(s):
		right = len(s) - 1
		left = starting_point

		while left < right:
			if s[left] == s[right]:
				ending_point = right
				max_length = ending_point - starting_point + 1
				between_letters = s[starting_point:ending_point + 1]
				left = ending_point
				right = len(s) - 1
				break
			elif left >= ending_point and s[right] in between_letters:
				ending_point = right
				max_length = ending_point - starting_point + 1
			else:
				right -= 1
	starting_point = ending_point + 1
	res.append(max_length)

	return res


s = 'ababcbacacdefegdehijhklij'
s1 = 'abca'


# print(func(s1))


def comparing_strings_backspaces(str1, str2):
	if not str1 or not str2:
		return False

	def helper(s):

		for i in range(len(s)):
			left = i
			right = 1
			while left < right:
				if s[right] == '#':
					if s[right - 1] == '#':
						right -= 1
						break
					else:
						s = s.replace(s[right], '')
						s = s.replace(s[right - 1], '', 1)
						break
				else:
					right -= 1
		return s

	return helper(str1) == helper(str2)


def build(string):
	ans = []
	for c in string:
		if c != '#':
			ans.append(c)
		elif ans:
			ans.pop()
	return ''.join(ans)


print(comparing_strings_backspaces("a#b#c", "ab##c"))
print(build('ab##c'))
