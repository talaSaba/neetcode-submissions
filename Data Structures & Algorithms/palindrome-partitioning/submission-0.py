class Solution:
    def partition(self, s: str) -> List[List[str]]:
        seen=set()
        cur=[]
        res=[]
        def check(s1,s2):
            return s1 == s1[::-1]
        def part(start):
            if start>=len(s) :
                ss=cur[::]
                for i in ss:
                    if check(i,i)==False:
                        return 
                res.append(ss)
                return 
            for i in range(start,len(s)):
                cur.append(s[start:i+1])
                part(i+1)
                cur.pop()
        part(0)
        return res

        
        

