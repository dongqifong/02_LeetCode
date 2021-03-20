class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x<0:
            return False
        if x>=0:
            reverse=str(x)[::-1]
            if reverse==str(x):
                return True
            else:
                return False
class Solution2:
    def isPalindrome(self, x: int) -> bool:
        if x<0:
            return False
        
        revert=0
        if x>=0:
            while x>revert:
                revert=revert*10+x%10
                x=int(x/10)
            print('----')
            print(revert)
            print(x)
            if revert==x or int(revert/10):
                return True
            else:
                return False

class Solution3:
    def isPalindrome(self, x: int) -> bool:
        if x%10==0 or x<0:
            return False
        reverse=0
        while x>reverse:
            reverse=reverse*10+x%10
            x=x//10
        print(x)
        print(reverse)
        return x==reverse or x==reverse//10

test=12321
s=Solution3()
print(s.isPalindrome(test))
