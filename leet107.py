# encoding: utf8
'''
Binary Tree Level Order Traversal II
For example:
Given binary tree {3,9,20,#,#,15,7},
    3
   / \
  9  20
    /  \
   15   7
return its level order traversal as:
[
  [15,7]
  [9,20],
  [3],
]
'''

import unittest
from pprint import pprint
import pdb

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    # @param {TreeNode} root
    # @return {integer[][]}
    def levelOrderBottom(self, root):
        self.ans=[]
        if root:
            self.go(root, 0)
        return self.ans[::-1]

    def go(self, root, level):
        try:
            self.ans[level].append(root.val)
        except Exception, e:
            self.ans.append([root.val])
        if root.left:
            self.go(root.left, level+1)
        if root.right:
            self.go(root.right, level+1)

class testCase(unittest.TestCase):
    def setUp(self):
        pass
        self.a=Solution()

    def testLeet(self):
        a=TreeNode(1)
        a.left=TreeNode(2)
        a.right=TreeNode(3)
        self.assertEqual(self.a.levelOrderBottom(a),[[2,3],[1]])


if __name__ == '__main__':
    unittest.main()