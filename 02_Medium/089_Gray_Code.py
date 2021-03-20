import os
import time
os.system('clear')

class Solution:
    def grayCode(self, n: int):
        combination=[0]
        for i in range(n):
            next_level=[ 2**i + r for r in combination[::-1]]
            combination += next_level
        return combination
    def grayCode2(self, n):
        return [(i>>1)^i for i in range(2**n)]
        # for i in range(1,2**n):
        #     res.append(res[-1]^(i&-i))
        # return res

n=10
s=Solution()

t1=time.time()
s.grayCode(n)

t2=time.time()

s.grayCode2(n)
t3=time.time()

print((t2-t1)/(t3-t2))
i=3
print(i & -i)

'''Explanation 1
就是歷史數字反轉過來在加上這一層(2**i)的底數
靠觀察出來的
'''


'''Explanation 2
def grayCode(self, n: int) -> 'List[int]':
	res = [0]
	for i in range(1, 2**n):
		res.append(res[-1] ^ (i & -i))
	return res

Fisrt, we can explore the data and try to figure out the pattern.
For example, when n=3, results start from 000, we can XOR last number in results with X .
result[i+1] = X[i] ^ result[i]
Below we can figure out the pattern of X:

result          X                  Y
0 0 0         0 0 1           0 0 1 (1)
0 0 1         0 1 0           0 1 0 (2)
0 1 1         0 0 1           0 1 1 (3)
0 1 0         1 0 0           1 0 0 (4)
1 1 0         0 0 1           1 0 1 (5)
1 1 1         0 1 0           1 1 0 (6)
1 0 1         0 0 1           1 1 1 (7)
1 0 0
So the keypoint is to generate X sequence. Here is the trick, actually X is lowest one-bit of Y (natural number set).
According to bit-manipulation, we can get lowest one-bit of number by
X = Y & -Y
Finally, we can get this elegant and easy-understand solution:


Awesome! Why does X = Y & -Y give us the lowest bit? Here is an explanation:

~Y inverts all bits. Also
~Y = -Y - 1 (widely used - hello Python's negative list indexes).
-Y = ~Y + 1 This will give us an idea of what -Y looks like in bin

0000000000000101 = Y
1111111111111010 = ~Y
1111111111111011 = ~Y + 1 = -Y

0000000000000001 = Y & -Y
'''