class Solution:
    def isPalindrome(self, s: str) -> bool:
        #s=s.lower()-----> creates a 
        # a=[]
        # for i in s:
        #     if i.isalnum():
        #         a.append(i)
        right=len(s)-1
        left=0
        while left<right:
            if s[left].isalnum() and s[right].isalnum():
                if s[left].lower()!=s[right].lower():
            #if a[left]!=a[right]:
                    return False
                left+=1
                right-=1
            elif not s[left].isalnum():
                left+=1
            else:
                right-=1

        return True        

