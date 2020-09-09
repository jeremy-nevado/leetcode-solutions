import unittest

class Solution:
    def merge_sort(self, lst):
        midpoint = len(lst)//2
        res = []
        if len(lst) == 0 or len(lst) == 1: return lst
        left = self.merge_sort(lst[:midpoint])
        right = self.merge_sort(lst[midpoint:])
        while left and right :
             if left[0] > right[0]:
                 res.append(right.pop(0)) 
             else: res.append(left.pop(0))
        res = res + (left or right)
        return res

class TestSolution(unittest.TestCase):
    def test_mergesort(self):
        self.assertEqual(Solution().merge_sort([3, 1, 5, 2]), [1, 2, 3, 5])
        self.assertEqual(Solution().merge_sort([2, 1, 3, 1, 5, 0, -4]), [-4, 0, 1, 1, 2, 3, 5])
        self.assertEqual(Solution().merge_sort([]), [])
        self.assertEqual(Solution().merge_sort([5]), [5])

if __name__ == '__main__':
    unittest.main()
