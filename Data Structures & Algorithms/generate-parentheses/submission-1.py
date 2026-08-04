class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        # we have here two decsiions:
        # the number of open has to be bigger than closed and we open , we delete the open then we close 

        curr=[]
        res=[]
        def back(open,close):
            if close<open:
                return
            if open==0 and close==0:
                strin="".join(curr)
                res.append(strin)
                return 
         
            if open>0:
                curr.append("(")
                back(open-1,close)
                curr.pop()
            if close>0:
                curr.append(")")
                back(open,close-1)
                curr.pop()
        back(n,n)
        return res

            
            
