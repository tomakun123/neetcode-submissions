from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        finder = defaultdict(list)

        for word in strs:
            sorted_word = "".join(sorted(word))
            finder[sorted_word].append(word)
        
        final = list(finder.values())
        
        return final