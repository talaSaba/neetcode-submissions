class Solution:
    def isPalindrome(self, s: str) -> bool:
        s=s.lower()
        a=[]
        for i in s:
            if i.isalnum():
                a.append(i)
        right=len(a)-1
        left=0
        while left<right:
            if a[left]!=a[right]:
                return False
            left+=1
            right-=1
        return True        

