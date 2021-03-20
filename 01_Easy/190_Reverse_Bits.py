'''
190. Reverse Bits
Reverse bits of a given 32 bits unsigned integer.
'''

class Solution:
    def reverseBits(self, n: int) -> int:
        ans=0
        for i in range(32):
            ans=(ans<<1)|(n & 1)
            n>>=1
        return ans


    