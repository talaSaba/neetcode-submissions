class Solution:
    def isValid(self, s: str) -> bool:
        stack=[]
        i=0
        while len(s)>i:
            if s[i]=='(' or s[i]=='{' or s[i]=='[':
                stack.append(s[i])
            elif len(stack)>0 and s[i]==']' and stack[-1]=='[':
                stack.pop()
            elif len(stack)>0 and s[i]==')' and stack[-1]=='(':
                stack.pop()
            elif len(stack)>0 and s[i]=='}' and stack[-1]=='{':
                stack.pop()
            else:
                return False
            i+=1
        return len(stack)==0
            
            
        