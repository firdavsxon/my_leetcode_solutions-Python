"""
Comparing Strings containing Backspaces (medium) #
Given two strings containing backspaces (identified by the character ‘#’),
check if the two strings are equal.

Example 1:

Input: str1="xy#z", str2="xzz#"
Output: true
Explanation: After applying backspaces the strings become "xz" and "xz" respectively.
Example 2:

Input: str1="xy#z", str2="xyz#"
Output: false
Explanation: After applying backspaces the strings become "xz" and "xy" respectively.
Example 3:

Input: str1="xp#", str2="xyz##"
Output: true
Explanation: After applying backspaces the strings become "x" and "x" respectively.
In "xyz##", the first '#' removes the character 'z' and the second '#' removes the
character 'y'.
Example 4:

Input: str1="xywrrmp", str2="xywrrmu#p"
Output: true
Explanation: After applying backspaces the strings become "xywrrmp" and "xywrrmp"
respectively.

"""

def comparing_strings_backspaces(str1, str2):
	if not str1 or not str2:
		return False

	def helper(s):

		for i in range(len(s)):
			left = i
			right = len(s) - 1
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


	return helper(str1)== helper(str2)

def backspace_compare(str1, str2):
	index1 = len(str1) -1
	index2 = len(str2) - 1

	while index1 >= 0 or index2>= 0:
		i1 = get_next_valid_char_index(str1, index1)
		i2 = get_next_valid_char_index(str2, index2)
		if i1 < 0 and i2<0:
			return True
		if i1 < 0 or i2<0:
			return False
		if str1[i1] != str2[i2]:
			return False

		index1 -= 1
		index2 -= 1
	return True



def get_next_valid_char_index(str, index):
	backspace_count = 0
	while index >= 0:
		if str[index] == '#':
			backspace_count += 1
		elif backspace_count >0:
			backspace_count -= 1
		else:
			break
		index -= 1

	return index


# print(comparing_strings_backspaces(str1="xy#z", str2="xzz#" ))
print(comparing_strings_backspaces(str1="ab#c", str2="ad#c" ))


