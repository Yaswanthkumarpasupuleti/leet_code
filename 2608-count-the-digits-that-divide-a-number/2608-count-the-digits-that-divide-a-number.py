class Solution:
    def countDigits(self, num: int) -> int:
        cnt = 0
        temp = num
        while num > 0:
            digit = num % 10
            if temp % digit == 0:
                cnt += 1
            num = num // 10
        return cnt
        