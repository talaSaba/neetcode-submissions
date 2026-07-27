class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        ss={}
        maxx=0
        left,right=0,0
        while left<len(s) and right<len(s) and left<=right:
            dd=ss.get(s[right],0)
            if dd==0:
                
                ss[s[right]]=1
                right+=1
                maxx=max(maxx,(right-left))
            else:
                maxx=max(maxx,(right-left))
                while s[left]!=s[right]:
                    ss[s[left]]-=1
                    left+=1
                ss[s[left]]-=1
                left+=1
        return maxx