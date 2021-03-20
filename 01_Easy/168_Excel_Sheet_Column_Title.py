'''
168. Excel Sheet Column Title
Given a positive integer, return its corresponding column title as appear in an Excel sheet.
'''

class Solution:
    def convertToTitle(self, n: int) -> str:
        result=''
        while n>0:
            letter_dec=(n-1)%26+65
            result+=chr(letter_dec)
            n=(n-1)//26