class Solution:
    def reverseWords(self, s: str) -> str:
        lst = s.split()
        res = ""
        for word in lst:
            word = word[::-1]
            res += word +" "
        return res[:-1]