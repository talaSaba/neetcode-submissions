class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        strin1=list(word1)
        strin2=list(word2)
        e=[]
        s1=0
        s2=0
        while s1<len(word1) and s2<len(word2):
            e.append(strin1[s1])
            e.append(strin2[s2])
            s1+=1
            s2+=1
        while s1<len(word1):
            e.append(word1[s1])
            s1+=1
        while s2<len(word2):
            e.append(word2[s2])
            s2+=1  
        return "".join(e)      
                
        