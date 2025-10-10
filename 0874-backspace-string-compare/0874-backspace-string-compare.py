class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        lst = []
        for char in s:
            if char == "#":
                if not lst:
                    continue
                else:
                    lst.pop()
            else:
                lst.append(char)
        s = str(lst)
        lst = []
        for char in t:
            if char == "#":
                if not lst:
                    continue
                else:
                    lst.pop()
            else:
                lst.append(char)
        t = str(lst)
        return s == t
        
        