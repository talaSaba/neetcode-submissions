class Solution:

    def encode(self, strs: List[str]) -> str:
        strr=""
        for i in strs:
            strr=strr+str(len(i))+"#"+i
        return strr    



    def decode(self, s: str) -> List[str]:
        listt=[]
        j=0
        while j<len(s):
            i=j
            while s[i]!="#":
                i+=1
            lenn=int(s[j:i])
            listt.append(s[i+1:i+1+lenn])
            j=i+lenn+1
        return listt        

