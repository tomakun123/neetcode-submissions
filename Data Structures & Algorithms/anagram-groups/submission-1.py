class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dic = {}

        for word in strs:
            sw = "".join(sorted(word))
            if sw not in dic:
                dic[sw] = []
            dic[sw].append(word)

        return list(dic.values())