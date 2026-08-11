class Solution:
    def isPalindrome(self, s: str) -> bool:
        begin = 0
        end = len(s)-1

        s=s.lower()
        slist = list(s)
        alpha = "abcdefghijklmnopqrstuvwxyz0123456789"

        while(begin < end):
            if (slist[begin] not in alpha):
                begin += 1
                continue
            elif (slist[end] not in alpha):
                end -= 1
                continue
            if (slist[begin] != slist[end]):
                return False
            else:
                begin += 1
                end -= 1
        return True