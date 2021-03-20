'''
56. Merge Intervals
Given an array of intervals where intervals[i] = [starti, endi], merge all overlapping intervals, and return an array of the non-overlapping intervals that cover all the intervals in the input.
'''
import os
os.system('cls')
class Solution:
    def merge(self, intervals):
        # intervals.sort()
        intervals=sorted(intervals)
        stack = [intervals[0]]
        for current in intervals[1:]:
            if current[0] <= stack[-1][1]: 
                stack[-1][1] = max(current[1], stack[-1][1])
            else: 
                stack.append(current)
        return stack
        
        

testcase1=[[1,3],[2,6],[8,10],[15,18]]#[[1,6],[8,10],[15,18]]
testcase2=[[1,4],[4,5]]#[[1,5]]
testcase3=[[1,2],[2,5],[5,5]]#[[1,5]]
testcase4=[[1,4],[0,4]]#[[0, 4]]
testcase5=[[1,4],[0,0]]#[[0, 0], [1, 4]]
testcase6=[[1,4],[0,2],[3,5]]#[[0, 5]]

s=Solution()
res=s.merge(testcase6)
print(res)
