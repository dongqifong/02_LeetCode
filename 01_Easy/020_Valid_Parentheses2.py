import os
if os.name=='nt':#windows
    os.system('cls')
else:
    os.system('clear')


class Solution():
    def isValid(self,s:str):
        rule={}
        rule["("]=")"
        rule["["]="]"
        rule["{"]="}"
        stack=[]
        s=list(s)
        while s:
            if not stack:
                if s[0] in rule:
                    stack.append(s.pop(0))
                    continue
                else:
                    return False
            if s[0] in rule:
                stack.append(s.pop(0))
            else:
                if rule[stack[-1]]==s[0]:
                    stack.pop()
                    s.pop(0)
                else:
                    return False
        if not stack:
            return True
        else:
            return False
