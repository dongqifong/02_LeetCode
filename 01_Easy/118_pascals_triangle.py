import os
os.system('clear')
class solution():
    def generate(self, numRows: int):
        if numRows==0:
            return []
        d=[[1]]
        if numRows==1:
            return d
        level=1
        while level<numRows:
            d.append([1])
            for i in range(level-1):
                num=d[level-1][i]+d[level-1][i+1]
                d[level].append(num)
            d[level].append(1)
            level+=1
        return d
s=solution()
print(s.generate(0))
print(s.generate(1))
print(s.generate(2))
print(s.generate(5))
