"""
Permutation in a String (hard) #
Given a string and a pattern, find out if the string contains any permutation of the pattern.

Permutation is defined as the re-arranging of the characters of the string. For example, “abc” has the following six permutations:

abc
acb
bac
bca
cab
cba
If a string has ‘n’ distinct characters it will have n!n! permutations.

Example 1:

Input: String="oidbcaf", Pattern="abc"
Output: true
Explanation: The string contains "bca" which is a permutation of the given pattern.
Example 2:

Input: String="odicf", Pattern="dc"
Output: false
Explanation: No permutation of the pattern is present in the given string as a substring.
Example 3:

Input: String="bcdxabcdy", Pattern="bcdyabcdx"
Output: true
Explanation: Both the string and the pattern are a permutation of each other.
Example 4:

Input: String="aacba", Pattern="abc"
Output: true
Explanation: The string contains "acb" which is a permutation of the given pattern.
"""


class Solution:
    def permutation(self, string, pattern):
        window_start = 0
        for window_end in range(len(string)):
            d = {}
            right_char= string[window_end]
            if right_char not in d:
                d[right_char] = 0
            d[right_char] += 1

            if len(d)==len(pattern):
                if set(d.keys())==set(pattern):
                    return True
                else:
                    left_char = string[window_start]
                    d[left_char]-=1
                    if d[left_char]==0:
                        del d[left_char]
        return False


string = 'aaacb'
pattern = 'abc'
test = Solution()
print(test.permutation(string, pattern))


def sherlockAndAnagrams(s):
    count = 0
    anagram_map = {}

    for i in range(1, len(s)):
        for j in range(len(s)-i+1):

            sorted_anagram = str(sorted(s[j:j+i]))
            if sorted_anagram not in anagram_map:
                anagram_map[sorted_anagram] = 1
            else:
                count+= anagram_map[sorted_anagram]
                anagram_map[sorted_anagram] += 1
    print(anagram_map)
    return count

# print(sherlockAndAnagrams('abba'))


def countTriplets(arr, r):

    # if len(arr) < 3:
    #     return 0
    # h = {}
    # for i in range(len(arr)):
    #     first = i
    #     second = i + 1
    #     third = i + 2
    #     while third < len(arr):
    #         if arr[first] * r == arr[second] and arr[second] * r == arr[third]:
    #             # out.append([first, second, third])
    #             triplet = (first, second, third)
    #             if triplet not in h:
    #                 h[triplet] = True
    #         third += 1
    #     third-=1
    #     while second < third:
    #         if arr[first] * r == arr[second] and arr[second] * r == arr[third]:
    #             # out.append([first, second, third])
    #             triplet = (first, second, third)
    #             if triplet not in h:
    #                 h[triplet] = True
    #         second += 1
    count = 0
    dict = {}
    dictPairs = {}

    for i in reversed(arr):
        if i * r in dictPairs:
            count += dictPairs[i * r]
        if i * r in dict:
            dictPairs[i] = dictPairs.get(i, 0) + dict[i * r]

        dict[i] = dict.get(i, 0) + 1

    return count
arr=[1,3,9,9,27,81]
r= 3
print(countTriplets(arr, r))

