'''
12. Integer to Roman
Roman numerals are represented by seven different symbols: I, V, X, L, C, D and M.
For example, 2 is written as II in Roman numeral, just two one's added together. 12 is written as XII, which is simply X + II. The number 27 is written as XXVII, which is XX + V + II.

Roman numerals are usually written largest to smallest from left to right. However, the numeral for four is not IIII. Instead, the number four is written as IV. Because the one is before the five we subtract it making four. The same principle applies to the number nine, which is written as IX. There are six instances where subtraction is used:

I can be placed before V (5) and X (10) to make 4 and 9. 
X can be placed before L (50) and C (100) to make 40 and 90. 
C can be placed before D (500) and M (1000) to make 400 and 900.
Given an integer, convert it to a roman numeral.
'''
class Solution:
    def intToRoman(self, num: int) -> str:
        letter=["I","V","X","L","C","D","M"]
        power=0
        result=''
        while num:
            d=num%10
            if 1<=d<=3:
                result=letter[power]*d+result
            elif d==4:
                result=letter[power]+letter[power+1]+result
            elif d==5:
                result=letter[power+1]+result
            elif 5<d<9:
                result=letter[power+1]+letter[power]*(d-5)+result
            elif d==9:
                result=letter[power]+letter[power+2]+result
            else:
                result=result
            if power<6:
                power+=2
            num=num//10
        return result
                
            
                
                
                
        