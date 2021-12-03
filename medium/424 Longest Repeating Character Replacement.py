"""

You are given a string s and an integer k. You can choose any character of the string and change it to any other uppercase English character. You can perform this operation at most k times.

Return the length of the longest substring containing the same letter you can get after performing the above operations.



Example 1:

Input: s = "ABAB", k = 2
Output: 4
Explanation: Replace the two 'A's with two 'B's or vice versa.
Example 2:

Input: s = "AABABBA", k = 1
Output: 4
Explanation: Replace the one 'A' in the middle with 'B' and form "AABBBBA".
The substring "BBBB" has the longest repeating letters, which is 4.


Constraints:

1 <= s.length <= 105
s consists of only uppercase English letters.
0 <= k <= s.length0
"""

def characterReplacement( s: str, k: int) -> int:
        max_l = 0
        # replacement = 0
        # if len(s)==1:
        #     return 1
        # for i in range(len(s)):
        #     left = i
        #     right = i+1
        #     while right<len(s):
        #         if s[right]==s[left]:
        #             max_l = max(max_l, right-left+1)
        #             right+=1
        #         else:
        #             if replacement<k:
        #                 max_l = max(max_l,right-left+1)
        #                 right+=1
        #                 replacement+=1
        #             else:
        #                 break
        # return max_l
        if len(s) == 1:
            return 1
        for i in range(len(s)):
            left = i
            temp = {}
            right = i + 1
            adding_to_map(s[left], temp)
            while right < len(s):
                while right < len(s):
                    if len(temp) <= 2:
                        adding_to_map(s[right], temp)
                    else:
                        left += 1
                        right = left + 1
                        break
                    minimum_replacement = min(temp.values())
                    if minimum_replacement <= k:
                        total_letter_count = sum(temp.values())
                        max_l = max(max_l, total_letter_count)
                    right += 1
        return max_l

def adding_to_map(letter, h_map):
    if letter not in h_map:
        h_map[letter] = 1
    else:
        h_map[letter] += 1


def max_repeat(s, k):
    window_start, max_l, max_repeating_letter_count = 0, 0,0
    frequency_map = {}

    for window_end in range(len(s)):
        right_char = s[window_end]
        if right_char not in frequency_map:
            frequency_map[right_char] = 0
        frequency_map[right_char] += 1
        max_repeating_letter_count = max(max_repeating_letter_count, frequency_map[right_char])
        if (window_end - window_start + 1 - max_repeating_letter_count) > k:
            left_char = s[window_start]
            frequency_map[left_char] -= 1
            window_start += 1
        max_l = max(max_l, window_end - window_start + 1)
    return max_l




s="AABABBA"
k=1
print(max_repeat(s, k))
