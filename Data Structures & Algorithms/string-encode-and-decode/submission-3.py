class Solution:

    def encode(self, strs: List[str]) -> str:
    #def encode(self, strs: List[str]) -> str:
        # strr = []

        # for i in strs:
        #     strr.append(str(len(i)) + "#" + i)

        # return "".join(strr) 
        str_ans=[]
        for stri in strs:
            str_ans.append(str(len(stri))+"#"+stri)
        return "".join(str_ans)    



    def decode(self, s: str) -> List[str]:
        # listt=[]
        # j=0
        # while j<len(s):
        #     i=j
        #     while s[i]!="#":
        #         i+=1
        #     lenn=int(s[j:i])
        #     listt.append(s[i+1:i+1+lenn])
        #     j=i+lenn+1
        # return listt  
        list_ans=[]
        j=0
        while j!=len(s):
            i=j
            while s[j]!='#':
                j+=1
            numb=int(s[i:j])
            d=s[j+1:j+numb+1]
            j=j+numb+1   
            list_ans.append(d)
        return list_ans


