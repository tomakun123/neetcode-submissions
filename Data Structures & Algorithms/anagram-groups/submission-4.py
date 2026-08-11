from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dic = defaultdict(list)

        for word in strs:
            sw = "".join(sorted(word))
            
            dic[sw] += [word]
        
        return list(dic.values())