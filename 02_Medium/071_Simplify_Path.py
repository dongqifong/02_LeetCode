'''
71. Simplify Path
Given a string path, which is an absolute path (starting with a slash '/') to a file or directory in a Unix-style file system, convert it to the simplified canonical path.

In a Unix-style file system, a period '.' refers to the current directory, a double period '..' refers to the directory up a level, and any multiple consecutive slashes (i.e. '//') are treated as a single slash '/'. For this problem, any other format of periods such as '...' are treated as file/directory names.

The canonical path should have the following format:

The path starts with a single slash '/'.
Any two directories are separated by a single slash '/'.
The path does not end with a trailing '/'.
The path only contains the directories on the path from the root directory to the target file or directory (i.e., no period '.' or double period '..')
Return the simplified canonical path.
'''

import os
os.system('cls')
class Solution:
    def simplifyPath(self, path: str) -> str:
        path=path.split('/')
        path.pop(0)
        if path[-1]=='':
            path.pop()
        
        #pop every '.'
        i=0
        while i<len(path):
            if path[i]=='.' or path[i]=='':
                path.pop(i)
            else:i+=1
        # pop '..' and last[i-1] content if exist
        i=0
        while i<len(path):
            if path[i]=='..':
                path.pop(i)
                if i-1>=0:
                    path.pop(i-1)
                    i=max(i-1,0)
            else:
                i+=1
        #connect final content to string
        ans='/'
        if path:
            ans=ans+'/'.join(path)
        return ans

# path="/home/"#"/home"
# path = "/../"#"/"
# path = "/home//foo/"#"/home/foo"
# path = "/a/./b/../../c/"#/c
# path='/'
# path="/home/../../.."
# path="/.///../JY"
s=Solution()
res=s.simplifyPath(path)
print(res)

'''
第一步先以'/'為分隔符號轉成陣列
第二步將前後方的空白剔除
第三步剔除陣列中'/'和'.'
第四步如果碰到..要剔除本身
若前面有內容，也要跟著剔除
最後，若陣列有值，合併成字串回傳否則回傳'/'
'''