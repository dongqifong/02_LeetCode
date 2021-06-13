'''
Given an input string s, reverse the order of the words.

A word is defined as a sequence of non-space characters. 
The words in s will be separated by at least one space.

Return a string of the words in reverse order concatenated by a single space.

Note that s may contain leading or trailing spaces or multiple spaces between two words. 
The returned string should only have a single space separating the words. 
Do not include any extra spaces.
'''

class Solution:
    def reverseWords(self, s: str) -> str:
        #先反轉字串
        s = s[::-1]
        result = ""
        l = 0
        r = 0
        while r<len(s):
            #找單詞區間步驟1: 找左邊界(l)
            if s[l] == " " and s[r] == " ":
                l += 1
                r += 1
                continue
            #找單詞區間步驟2: 找右邊界(r)
            if s[l]!=" " and (r+1)<len(s) and s[r+1]!=" ":
                r += 1 # r向前一步，直到r+1的位置是space，那l~r就是單詞區間
            
            #找到後反轉單詞並接上" "後，接到result上
            else:
                temp = s[l:r+1]
                result += temp[::-1] + " "
                l = r + 1
                r = r + 1
        return result[:-1] #去掉尾部空格並回傳

'''
先把原始的字串反轉
之後對每一個單詞逐一反轉

比方說:
s = "the sky is blue" 先轉成 
s2 = "eulb si yks eht"
之後再把eulb si yks eht這四個單次逐一反轉變成
blue is sky the
只是要注意空格


踢出多餘空格的方法就指定兩個指標l,r
先把l,r一起移到有字元的位置上
再移動r到第i的位置上，i+1要是空的
這樣代表位置l~r(包含)的區間是一個單詞
再把這個單辭反轉後接" "
再接到result上

最後把result的最後一個位置剔除，因為一定是空格(" ")
如此不用額外宣告陣列儲存單詞，所以空間複雜度是O(1)
而因為會遍歷整個s長度，所以時間複雜度是O(n)

其實花比較多時間的地方是在想，怎麼切出單詞區間l,r，要分兩步
'''