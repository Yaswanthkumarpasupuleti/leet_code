class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        for i in range(31):
            ans = 3 ** i
            if ans == n:
                return True
        return False
        