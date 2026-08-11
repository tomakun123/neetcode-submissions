class Solution:
    def isValid(self, s: str) -> bool:
        openChar = "([{"
        charDic = {
            "(" : ")",
            "[" : "]",
            "{" : "}",
            ")" : "(",
            "]" : "[",
            "}" : "{"
        }
        queue = []
        s = list(s)
        if len(s) < 2:
            return False
        for i in range(len(s)):
            if s[i] in openChar:
                queue.append(s[i])
            else:
                queue.append(s[i])
                if queue[len(queue)-1]==")" and queue[len(queue)-2]=="(":
                    queue.pop()
                    queue.pop()
                elif queue[len(queue)-1]=="]" and queue[len(queue)-2]=="[":
                    queue.pop()
                    queue.pop()
                elif queue[len(queue)-1]=="}" and queue[len(queue)-2]=="{":
                    queue.pop()
                    queue.pop()
        print(queue)
        if len(queue)==0:
            return True
        else:
            return False