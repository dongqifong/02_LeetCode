'''
171. Excel Sheet Column Number
Given a column title as appear in an Excel sheet, return its corresponding column number.
'''

class Solution:
    def titleToNumber(self, s: str) -> int:
        result=0
        power=0
        for i in range(len(s)-1,-1,-1):
            result+=(ord(s[i])-64)*26**power
            power+=1
        return result