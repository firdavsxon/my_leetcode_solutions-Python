class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1 or numRows == len(s):
            return s
        arr = ['']*numRows
        cycle = 0
        j=0
        for i in range(len(s)):
            arr[j] = arr[j]+ s[i]
            if not cycle:
                j = j+1
            else:
                j = j-1
            if j+1 == numRows:
                cycle = 1
            if j == 0:
                cycle = 0
        return ''.join(arr)

test = Solution()
s = "PAYPALISHIRING"
print(test.convert(s, numRows=3))



array = [3,6,1,3,6,6,3]

def find_unique(array):
    from collections import Counter
    h_map = Counter(array)
    for key in h_map:
        if h_map[key]==1:
            return key

        
print(find_unique(array))





