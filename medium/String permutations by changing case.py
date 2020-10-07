"""
Problem Statement #
Given a string, find all of its permutations preserving the character sequence but changing case.

Example 1:

Input: "ad52"
Output: "ad52", "Ad52", "aD52", "AD52"
Example 2:

Input: "ab7c"
Output: "ab7c", "Ab7c", "aB7c", "AB7c", "ab7C", "Ab7C", "aB7C", "AB7C"
"""

def find_letter_case_string_permutations(string):
	permutations = []
	permutations.append(string)
	for i in range(len(string)):
		if string[i].isalpha():
			n = len(permutations)
			for j in range(n):
				chs = list(permutations[j])
				chs[i] = chs[i].swapcase()
				permutations.append(''.join(chs))
	return permutations


print(find_letter_case_string_permutations("a1b"))
