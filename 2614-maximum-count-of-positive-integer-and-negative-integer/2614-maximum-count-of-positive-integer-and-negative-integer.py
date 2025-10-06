class Solution:
    def maximumCount(self, nums: List[int]) -> int:
        pc = nc = 0
        for ele in nums:
            if ele > 0:
                pc+=1
            elif ele < 0:
                nc += 1
            else:
                continue
        return pc if pc > nc else nc
        