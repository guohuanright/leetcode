# encoding: utf8
'''
Remove Element  
Given an array and a value, remove all instances of that value in place and return the new length.

The order of elements can be changed. It doesn't matter what you leave beyond the new length.

思路类似 leetcode 26 Remove Duplicates from Sorted Array
'''

import unittest
from pprint import pprint
import pdb

class Solution:
    # @param    A       a list of integers
    # @param    elem    an integer, value need to be removed
    # @return an integer
    def removeElement(self, A, elem):
        ll=len(A)
        i=0
        j=0
        while j<ll:
            if A[j]==elem:
                j+=1
            else:
                A[i]=A[j]
                i+=1
                j+=1
        # print A
        return i

class testCase(unittest.TestCase):
    def setUp(self):
        pass
        self.a=Solution()

    def testLeet(self):
        self.assertEqual(self.a.removeElement([1,2,2],1),2)
        self.assertEqual(self.a.removeElement([4,5],4),1)

if __name__ == '__main__':
    unittest.main()