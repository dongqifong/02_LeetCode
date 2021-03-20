'''
57. Insert Interval
Given a set of non-overlapping intervals, insert a new interval into the intervals (merge if necessary).

You may assume that the intervals were initially sorted according to their start times.
'''
import os
os.system('clear')
class Solution:
    def insert(self, intervals, newInterval):
        if not intervals:
            return [newInterval]
        intervals.append(newInterval)
        intervals=sorted(intervals)
        ans=[]
        ans.append(intervals[0])
        for i in range(1,len(intervals)):
            if ans[-1][1]>=intervals[i][0]:
                ans[-1][1]=max(ans[-1][1],intervals[i][1])
            else:
                ans.append(intervals[i])
        return ans

testcase1=[[[1,3],[6,9]],[2,5]]
testcase2=[[[1,2],[3,5],[6,7],[8,10],[12,16]],[4,8]]
testcase3=[[],[5,7]]
testcase4=[[[1,5]],[2,3]]
testcase5=[[[1,5]],[2,7]]

s=Solution()
res=s.insert(testcase1[0],testcase1[1])
print(res)

'''
觀念和上一題(056)一樣
只是多先插入newInterval再排序
'''