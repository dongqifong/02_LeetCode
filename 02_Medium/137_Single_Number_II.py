import os
os.system("clear")
class Solution:
    def singleNumber(self, nums):
        counterone=0
        countertwo=0
        for i in range(len(nums)):
            print("="*20)
            print("cur = ",nums[i])
            counterone=(~countertwo) & (counterone^nums[i])
            print("counterone = ",counterone)
            # print("~counterone = ",~counterone)
            countertwo=(~counterone) & (countertwo^nums[i])
            print("countertwo = ",countertwo)
            # print("~countertwo = ",~countertwo)
        return counterone


nums=[2,2,2,3]

s=Solution()
res=s.singleNumber(nums)
print("="*20)
print("res = ",res)

'''
簡單講，但並不完全正確
countone顯示出現一次的element
counttwo顯示出現兩次的element
出現三次就歸零，也就是兩兩一組看

或是說
如果其實出現三次了
counterone以為只有出現一次，無法辨別出現第三次
要靠countertwo的紀錄把他消除
消除的手法是&(~countertwo)

countertwo則是出現一次的話要，要靠&(~countone)消除
出現第三次，本身就可以依靠^消除
'''