"""
The string "PAYPALISHIRING" is written in a zigzag pattern on a given number of rows like this: (you may want to display this pattern in a fixed font for better legibility)
"""
class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows==1 or numRows==0:
            return s
        L=['']*numRows
        row=0
        step=1
        for i in s:
            L[row]+=i
            if row>=(numRows-1):
                step=step*-1
            row+=step
            if row<=0:
                step=1
        return ''.join(L)        