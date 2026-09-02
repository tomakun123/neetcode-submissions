from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        org = defaultdict(list)
        for word in strs:

            if "".join(sorted(word)) not in org:
                org["".join(sorted(word))] = [word]
            else:
                org["".join(sorted(word))] += [word]
        return list(org.values())
