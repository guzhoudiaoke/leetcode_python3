import copy
import time
import random

class Solution:
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
#        results = []
#        def solve(begin, current, tar):
#            if tar == 0:
#                ans = copy.deepcopy(current)
#                results.append(ans)
#                return
#
#            for i in range(begin, len(candidates)):
#                c = candidates[i]
#                if c <= tar:
#                    current.append(c)
#                    solve(i, current, tar-c)
#                    current.pop()
#
#        cur = []
#        solve(0, cur, target)
#        return results

        results = []
        def solve(begin, current, tar):
            if tar == 0:
                results.append(current)
                return

            for i in range(begin, len(candidates)):
                c = candidates[i]
                if c <= tar:
                    solve(i, current + [c], tar-c)

        solve(0, [], target)
        return results


    def combinationSum2(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        results = []
        def solve(begin, current, tar):
            if tar == 0:
                results.append(current)
                return

            for i in range(begin, len(candidates)):
                c = candidates[i]
                if c <= tar:
                    solve(i, current + [c], tar-c)

        cur = []
        solve(0, cur, target)
        return results


sol = Solution()

cands = [2, 3, 6, 7]
target = 7
ans = sol.combinationSum(cands, target)
print(ans)

cands = [2, 3, 5]
target = 8
ans = sol.combinationSum(cands, target)
print(ans)


cands = [random.randint(1, 100) for c in range(10)]
print(cands)
cands.sort()
print(cands)
target = random.randint(200, 1000)

start_time = time.clock()
ans = sol.combinationSum(cands, target)
end_time = time.clock()
print(end_time - start_time)

start_time = time.clock()
ans = sol.combinationSum2(cands, target)
end_time = time.clock()
print(end_time - start_time)

