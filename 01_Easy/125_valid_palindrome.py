'''
Given a string, determine if it is a palindrome, considering only alphanumeric characters and ignoring cases.

Note: For the purpose of this problem, we define empty string as valid palindrome.

Example 1:

Input: "A man, a plan, a canal: Panama"
Output: true
'''

import os

if os.name=='nt':
    os.system('cls')
else:
    os.system('clear')

class Solution:
    def isPalindrome(self, s):
        r=s.lower()
        L=0
        R=len(r)-1
        while L<R:
            if not r[L].isalnum():
                L+=1
                continue
            if not r[R].isalnum():
                R-=1
                continue
            if r[L]!=r[R]:
                return False
            else:
                L+=1
                R-=1
        return True
    
test1="A man, a plan, a canal: Panama"
test2="0p"
s=Solution()
print('test1=',s.isPalindrome(test1))
print('test2=',s.isPalindrome(test2))


