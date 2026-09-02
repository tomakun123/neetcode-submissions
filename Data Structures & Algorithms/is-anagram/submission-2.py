from collections import defaultdict
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s1 = defaultdict(str)
        s2 = defaultdict(str)
        for let in s:
            if let not in s1:
                s1[let] = 1
            else:
                s1[let] += 1
        for let in t:
            if let not in s2:
                s2[let] = 1
            else:
                s2[let] += 1
        
        if s1 != s2:
            return False
        return True