class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        has=Counter(s1)
        left, right=0,0
        while right<len(s2):
            while left <len(s2) and left==right and s2[left] not in has:
                left+=1
                right+=1
            if right<len(s2) and has[s2[right]]>0:
                has[s2[right]]-=1
                
                if right-left+1==len(s1):
                    return True
                right+=1
            elif right < len(s2):
                while left<right and s2[left]!=s2[right]:
                    has[s2[left]]+=1
                    left+=1
                has[s2[left]]+=1
                left+=1
                

        return False


