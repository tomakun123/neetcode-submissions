class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        used = []
        for i in range(len(s)):
            used.append(s[i])
        
        for i in range(len(t)):
            if t[i] in used:
                used.remove(t[i])
            else:
                return False
        if len(used) == 0:
            return True
        else:
            return False