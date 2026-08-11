from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dic = defaultdict(list)

        for word in strs:
            sw = "".join(sorted(word))
            dic[sw] += [word]

        print(str(dic.values()))
        
        return list(dic.values())