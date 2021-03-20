'''
49. Group Anagrams
Given an array of strings strs, group the anagrams together. You can return the answer in any order.

An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.
'''
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        ans=[]
        seen={}
        i=0
        for item in strs:
            temp="".join(sorted(item))
            if temp not in seen:
                ans.append([])
                seen[temp]=i
                ans[i].append(item)
                i+=1
            else:
                ans[seen[temp]].append(item)
        return ans

'''
go through each item in strs
sort this item

put hasn't seen word in dictionary "seen" 
or
append this item in array "ans"

return ans
'''