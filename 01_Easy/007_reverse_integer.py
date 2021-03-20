class Solution:
    def reverse(self, x: int) -> int:
        if x>=0:
            x_list=list(str(x))
        else:
            x_list=list(str(x))[1:]
        print(x_list)
        L=len(x_list)
        for i in range(L//2):
            x_list[i],x_list[L-i-1]=x_list[L-i-1],x_list[i]
        rev=''
        for i in range(L):
            rev+=x_list[i]
        if x>=0:
            return int(rev)
        else:
            return -int(rev)


class Solution2:
    def reverse(self, x: int) -> int:
        if x >= 2**31-1 or x <= -2**31: return 0
        else:
            strg = str(x)
            print(strg)
            if x >= 0 :
                revst = strg[::-1]
            else:
                temp = strg[1:] 
                temp2 = temp[::-1] 
                revst = "-" + temp2
            if int(revst) >= 2**31-1 or int(revst) <= -2**31: return 0
            else: return int(revst)
test=-123
s=Solution()

print(s.reverse(test))
