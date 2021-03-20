import os
os.system('clear')
class Solution:
    def exist(self, board, word) -> bool:
        m=len(board)
        n=len(board[0])
        w_list=list(word)
        direction=[[0,1],[1,0],[0,-1],[-1,0]]
        for i in range(m):
            for j in range(n):
                if board[i][j]==w_list[0]:
                    record=[[0]*n for k in range(m)]
                    if len(w_list)==1:
                        return True
                    else:
                        res=self.dfs(i,j,board,w_list,record,direction)
                        if res==True:
                            return res
        return False
    def dfs(self,r,c,board,w_list,record,direction):
        if len(w_list)==1:
            return True
        else:
            m=len(board)
            n=len(board[0])
            record[r][c]=1
            res=False
            for d in direction:
                next_r=r+d[0]
                next_c=c+d[1]
                if next_r<m and next_r>=0 and next_c<n and next_c>=0 and record[next_r][next_c]==0 and board[next_r][next_c]==w_list[1]:
                    res=res or self.dfs(next_r,next_c,board,w_list[1:],record,direction)
                    record[next_r][next_c]=0
            return res

# board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]]
# word = "ABCCED"
# board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]]
# word = "SEE"
# board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]]
# word = "ABCB"
# board=[['a','a']]
# word='aaa'
# board=[
# ["A","B","C","E"],
# ["S","F","E","S"],
# ["A","D","E","E"]]
# word="ABCEFSADEESE"
board=[
["a","a","a","a"],
["a","a","a","a"],
["a","a","a","a"]
]
word="aaaaaaaaaaaaaaa"
s=Solution()
res=s.exist(board,word)
print(res)

'''
主要是走地圖的概念
但是起點是要先走訪過每一格
當某一個是word的第一個字母
該格是為起點
接著用dfs向外拓展搜尋
但要注意的是
dfs方法立面
每個方向走完
要把剛剛走過的方法復原回去
不然會擋住其他路徑到達那個地方的去向

'''