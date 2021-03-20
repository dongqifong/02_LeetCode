import os
if os.name=="nt":
    os.system('cls')
else:
    os.system('clear')

class Solution:
    def merge(self, nums1, m, nums2, n) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        while m > 0 and n > 0:
            if nums1[m-1] >= nums2[n-1]:
                nums1[m+n-1] = nums1[m-1]
                m -= 1
            else:
                nums1[m+n-1] = nums2[n-1]
                n -= 1
        if n > 0:
            nums1[:n] = nums2[:n]
num1 = [1,2,3,0,0,0]
m = 3
num2 = [2,5,6]
n = 3


s=Solution()
s.merge(num1,m,num2,n)
print(num1)