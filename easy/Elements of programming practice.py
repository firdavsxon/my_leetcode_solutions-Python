"""

Given a 2d grid map of '1's (land) and '0's (water), count the number of islands. An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically. You may assume all four edges of the grid are all surrounded by water.



Example 1:

Input: grid = [
  ["1","1","1","1","0"],
  ["1","1","0","1","0"],
  ["1","1","0","0","0"],
  ["0","0","0","0","0"]
]
Output: 1
Example 2:

Input: grid = [
  ["1","1","0","0","0"],
  ["1","1","0","0","0"],
  ["0","0","1","0","0"],
  ["0","0","0","1","1"]
]
Output: 3

"""
from typing import List


def numIslands(grid: List[List[int]]):
    if not grid:
        return 0

    nr = len(grid)
    nc = len(grid[0])
    visited = {}
    population = 0
    for r in range(nr):
        for c in range(nc):
            if grid[r][c] != 0 and str(r) + str(c) not in visited:
                dfs(grid, r, c, visited, population)
    return population


def dfs(matrix, r, c, visited, population):
    nr = len(matrix)
    nc = len(matrix[0])

    if r < 0 or c < 0 or r >= nr or c >= nc or matrix[r][c] == 0:
        return

    population += matrix[r][c]
    visited[str(r) + str(c)] = population
    dfs(matrix, r - 1, c, visited, population)
    dfs(matrix, r + 1, c, visited, population)
    dfs(matrix, r, c - 1, visited, population)
    dfs(matrix, r, c + 1, visited, population)


# print(numIslands([[1, 2, 3, 0, 0],
# 				  [0, 0, 0, 9, 0],
# 				  [3, 4, 0, 0, 2]]))


# Singly-linked lists are already defined with this interface:
class ListNode(object):
    def __init__(self, x):
        self.value = x
        self.next = None


#   prev-> 2 -> 3 -> 2
def removeKFromList(l, k):
    if not l:
        return None
    if l.value == k:
        l = l.next
        if l is None:
            return None
    current = l
    while current.next:
        if current.value == k:
            current.value = current.next.value
            current.next = current.next.next
        else:
            current = current.next
    if current.value == k and current.next is None:
        l = remove_last(l)
    p = l
    while p:
        print(p.value, end=" -> ")
        p = p.next


def remove_last(head):
    if not head:
        return None
    if head.next is None:
        head = None
        return None
    p = head
    while p.next.next:
        p = p.next
    p.next = None
    return head
def is_palindrome(l):
    fast = slow= l
    current = l
    while fast.next.next:
        fast = fast.next.next
        slow = slow.next


    reversed_half = reverse_node(slow)

    while reversed_half:
        if current.value!= reversed_half.value:
            return False
        current = current.next
        reversed_half = reversed_half.next
    return True

def reverse_node(node):
    current = node
    prev = None
    while current:
        temp = current.next
        current.next = prev
        prev = current
        current = temp
    return prev


def main():
    head = ListNode(0)
    head.next = ListNode(1)
    head.next.next = ListNode(2)
    head.next.next.next = ListNode(2)
    head.next.next.next.next = ListNode(1)
    head.next.next.next.next.next = ListNode(0)

    print("Given list: ")
    current = head
    while current:
        print(current.value, end=" -> ")
        current = current.next
    print()
    print("After removing k in the list: ")

    # removeKFromList(head, 3)
    print("Palindrome?: ")
    print(is_palindrome(head))
    while current:
        print(current.value, end=" -> ")
        current = current.next


# main()

def parity(x:int)->int:
    result = 0
    while x:
        result ^= x & 1
        x >>= 1
    return result

def parity1(x:int)->int:
    result = 0
    while x:
        result ^= 1
        x &= x - 1
    return result

# def parity_cashing(x:int)->int:
# 	mask_size = 16
# 	bit_mask = 0xFFFF
# 	return (PRECOMPUTED_PARITY[x>>(3*mask_size)] ^
# 			PRECOMPUTED_PARITY[(x>>(2*mask_size)) & bit_mask] ^
# 			PRECOMPUTED_PARITY[(x>>mask_size)&bit_mask]^
# 			PRECOMPUTED_PARITY[x&bit_mask])
def swap_bits(x, i, j):
    # extract the i-th and j-th bits, and see if they differ.
    if  (x>>i) & 1 != (x>>j) & 1:
        # i-th and j-th bits differ. We will swap them by flipping their values.
        #Select the bits to flip with bit_mask. Since x^1=0 when x=1 and 1 when x=0,
        # we can perform the flip XOR
        bit_mask = (1 << i) | (1 << j)
        x ^= bit_mask
    return x

def dutch_flag(pivot_index, A):
    pivot = A[pivot_index]
    for i in range(len(A)):
        for j in range(i+1, len(A)):
            if A[j] < pivot:
                A[i], A[j] = A[j], A[i]
                break
    for i in reversed(range(len(A))):
        for j in reversed(range(i)):
            if A[j] > pivot:
                A[i], A[j] = A[j], A[i]
                break
    return A

def dutch_flag1(pivot_index: int, A: List[int]):
    pivot = A[pivot_index]
    left = 0
    right = len(A)-1
    for i, num in enumerate(A):
        if num < pivot:
            A[i], A[left] = A[left], A[i]
            left +=1
    for j in reversed(range(len(A))):
        if A[j] > pivot:
            A[j], A[right] = A[right], A[j]
            right -= 1
    return A


print(dutch_flag1(1, [1, 0, 0,1,1, 2, 2, 0, 2]))





