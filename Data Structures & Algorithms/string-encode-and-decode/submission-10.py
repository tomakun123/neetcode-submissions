import random
class Solution:

    # Encoder should be good
    def encode(self, strs: List[str]) -> str:
        # input --> ["Hello", "World"]
        msg = ""
        for i in range(len(strs)):
            length = len(strs[i])
            msg += (f"{length}:{strs[i]}")
            
        # return --> "5:Hello5:World"
        return msg

    # Working on this
    def decode(self, s: str) -> List[str]:
        # input --> "5:Hello5:World"
        # idea: 2 pointers: ind (default), j (number)
        #       ind++ until we find delimiter
        #       jump from i to j and store in between
        #12:awesomesauce4:fell
        fin = []
        ind = 0
        print(s)
        while ind < len(s):
            j = ind

            while s[j] != ":":
                j += 1

            length = int(s[ind:j])

            fin.append(s[j+1 : j+1+length])

            ind = j+1+length
            
        return fin

        