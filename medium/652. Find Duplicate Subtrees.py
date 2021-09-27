"""
Given the root of a binary tree, return all duplicate subtrees.

For each kind of duplicate subtrees, you only need to return the root node of any one of them.

Two trees are duplicate if they have the same structure with the same node values.



Example 1:


Input: root = [1,2,3,4,null,2,4,null,null,4]
Output: [[2,4],[4]]
Example 2:


Input: root = [2,1,1]
Output: [[1]]
Example 3:


Input: root = [2,2,2,3,null,3,null]
Output: [[2,3],[3]]


Constraints:

The number of the nodes in the tree will be in the range [1, 10^4]
-200 <= Node.val <= 200
"""
from typing import Optional, List

# Definition for a binary tree node.


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def findDuplicateSubtrees(self, root: Optional[TreeNode]) -> List[Optional[TreeNode]]:
        from collections import defaultdict
        h_map = defaultdict(lambda: 0)
        output = set()
        def dfs(h_map, root, output):
            if root:
                left = dfs(h_map, root.left, output)
                right = dfs(h_map, root.right, output)
                subtree = (root.val, left, right)
                val=root.val

                h_map[root.val] += 1
                if h_map[root.val] == 2:
                    output.add(root)
                    return subtree
            return None
        dfs(h_map, root, output)
        return list(output)


        #
        #
        #     if root:
        #         if root.val not in h_map:
        #             h_map[root.val] = [root.val]
        #             if root.left:
        #                 h_map[root.val].append(root.left.val)
        #                 dfs(h_map, root.left)
        #             else:
        #                 return
        #             if root.right:
        #                 h_map[root.val].append(root.right.val)
        #                 if root.right:
        #                     dfs(h_map, root.right)
        #             else:
        #                 if h_map[root.val]==[root.val, root.left.val]:
        #                     output.append(h_map[root.val])
        #                     output.append([root.left.val])
        #                 elif h_map[root.val] == [root.val, root.right.val]:
        #                     output.append(h_map[root.val])
        #                     output.append([root.right.val])
        #
        #
        #
        # dfs(h_map, root)
        # return output

test = Solution()
root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.right.left = TreeNode(2)
root.right.right = TreeNode(4)
root.right.left.left = TreeNode(4)
print(test.findDuplicateSubtrees(root))
root = [1,2,3,4,None,2,4,None,None,4]
