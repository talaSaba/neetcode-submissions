class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        cur=[]
        res=[]

        def back(i):
            if i>=len(s) and len(cur)==4:
                d=cur[:]
                dd=".".join(d)
                res.append(dd)
                return
            for d in range(i+1,min(i+4,len(s)+1)):
                a=s[i:d]
                if len(a) > 1 and a[0] == "0":
                    continue
                ddd=int(a)
                if ddd>=0 and ddd<=255:
                    cur.append(a)
                    back(d)
                    cur.pop()
        back(0)
        return res
            