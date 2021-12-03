"""
You are given an array and you need to find number of tripets of indices  such that the elements at those indices are in geometric progression for a given common ratio  and .

Example


There are  and  at indices  and . Return .

Function Description

Complete the countTriplets function in the editor below.

countTriplets has the following parameter(s):

int arr[n]: an array of integers
int r: the common ratio
Returns

int: the number of triplets
Input Format

The first line contains two space-separated integers  and , the size of  and the common ratio.
The next line contains  space-seperated integers .

Constraints

Sample Input 0

4 2
1 2 2 4
Sample Output 0

2
Explanation 0

There are  triplets in satisfying our criteria, whose indices are  and

Sample Input 1

6 3
1 3 9 9 27 81
Sample Output 1

6
Explanation 1

The triplets satisfying are index , , , ,  and .

Sample Input 2

5 5
1 5 5 25 125
Sample Output 2

4
Explanation 2

The triplets satisfying are index , , , .
"""

def countTriplets(arr, r):
    count = 0
    h_map = {}
    h_map_pairs = {}
    for i in reversed(arr):
        if i*r in h_map_pairs:
            count+= h_map_pairs[i*r]
        if i*r in h_map:
            h_map_pairs[i] = h_map_pairs.get(i,0) + h_map[i*r]
        h_map[i] = h_map.get(i,0)+1
    print(h_map)
    print(h_map_pairs)
    return count


arr = [1,3,9,9,27,81]
r = 3

print(countTriplets(arr,r))
