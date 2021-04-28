"""
Given a string str and array of pairs that indicates which indices in the string can be swapped, return the lexicographically largest string that results from doing the allowed swaps. You can swap indices any number of times.

Example

For str = "abdc" and pairs = [[1, 4], [3, 4]], the output should be
swapLexOrder(str, pairs) = "dbca".

By swapping the given indices, you get the strings: "cbda", "cbad", "dbac", "dbca". The lexicographically largest string in this list is "dbca".

Input/Output

[execution time limit] 4 seconds (py3)

[input] string str

A string consisting only of lowercase English letters.

Guaranteed constraints:
1 ≤ str.length ≤ 104.

[input] array.array.integer pairs

An array containing pairs of indices that can be swapped in str (1-based). This means that for each pairs[i], you can swap elements in str that have the indices pairs[i][0] and pairs[i][1].

Guaranteed constraints:
0 ≤ pairs.length ≤ 5000,
pairs[i].length = 2.

[output] string

"""

s = "abdc"
pairs = [[1, 4], [3, 4]]

s1 = "acxrabdz"
pairs1 = [[1, 3],
		  [6, 8],
		  [3, 8],
		  [2, 7]]


def build_permitted_subs(pairs):
	perm = []

	for a, b in pairs:
		merged = False
		for ind, sub_perm in enumerate(perm):
			if a in sub_perm or b in sub_perm:
				sub_perm.add(a)
				sub_perm.add(b)
				merged = True
				break

		else:
			perm.append({a, b})

		if merged:
			for merge_perm_ind in reversed(range(ind + 1, len(perm))):
				if perm[merge_perm_ind] & sub_perm:
					sub_perm.update(perm[merge_perm_ind])
					perm.pop(merge_perm_ind)

	return list(map(sorted, perm))


def swap_lex_order(swap_str, _pairs):
	pairs = [[a - 1, b - 1] for a, b in _pairs]
	out = list(swap_str)

	perm = build_permitted_subs(pairs)

	for sub_perm in perm:
		sorted_subset = sorted(sub_perm, key=lambda ind: swap_str[ind], reverse=True)

		for sort, targ in zip(sorted_subset, sub_perm):
			out[targ] = swap_str[sort]

	return "".join(out)


print(swap_lex_order(s1, pairs1))
