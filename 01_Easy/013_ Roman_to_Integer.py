class Solution2:
    def romanToInt(self, s: str) -> int:
        dic={}
        dic['I']=1
        dic['V']=5
        dic['X']=10
        dic['L']=50
        dic['C']=100
        dic['D']=500
        dic['M']=1000
        sum=0
        i=0
        while i<len(s):
            key_current=s[i]
            current_v=dic[key_current]
            if i<len(s)-1:
                key_next=s[i+1]
                next_v=dic[key_next]
                if current_v<next_v:
                    sum+=(next_v-current_v)
                    i+=1
                else:
                    sum+=current_v
            else:
                sum+=current_v
            i+=1
        return sum
s=Solution2()
result=s.romanToInt("MCMXCIV")
print(result)
result=s.romanToInt("III")
print(result)
