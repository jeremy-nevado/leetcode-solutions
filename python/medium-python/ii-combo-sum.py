import unittest


class Solution:
    def combinationSum2(self, candidates, target):
        def comboHelper(index, candidates, target, accum, res):
            if target == 0:
                res.append(accum)
                return
            for i in range(index, len(candidates)):
                if i > index and candidates[i] == candidates[i - 1]:
                    continue
                if candidates[i] > target:
                    break
                comboHelper(i + 1, candidates, target - candidates[i], accum + [candidates[i]], res)

        candidates.sort()
        res = []
        comboHelper(0, candidates, target, [], res)
        return res


class TestSolution(unittest.TestCase):
    def testComboSum2(self):
        self.assertEqual(Solution().combinationSum2(
            [10, 1, 2, 7, 6, 1, 5], 8),
            [[1, 7], [1, 2, 5], [2, 6], [1, 1, 6]]
            )


if __name__ == '__main__':
    unittest.main()
