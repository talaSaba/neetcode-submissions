
        # left,right=0,0
        # has={}
        # maxLength=0
        # #key='A'
        # for i in s:
        #     has[i]=0
        # while right<len(s) and left<=right:
        #     key = max(has, key=has.get)
        #     candidateMax = max(has[key], has[s[right]] + 1)
        #     if key==s[right]:
        #         has[key]+=1
                
        #         right+=1
        #         maxLength=max(maxLength,right-left)
                
        #     elif right-left-candidateMax<=k:
        #         has[s[right]]+=1
                
        #         right+=1
        #         maxLength=max(maxLength,right-left)
                
        #     else:
        #         while right-left-candidateMax+1>k:
        #             has[s[left]]-=1
        #             left+=1
        #             key = max(has, key=has.get)
        #             candidateMax = max(has[key], has[s[right]] + 1)
        #             #maxLength=max(maxLength,right-left)
        # return maxLength

class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        left, right = 0, 0
        has = {}
        maxLength = 0

        for char in s:
            has[char] = 0

        while right < len(s) and left <= right:
            key = max(has, key=has.get)

            candidateMax = max(
                has[key],
                has[s[right]] + 1
            )

            if right - left + 1 - candidateMax <= k:
                has[s[right]] += 1
                right += 1
                maxLength = max(maxLength, right - left)

            else:
                while right - left + 1 - candidateMax > k:
                    has[s[left]] -= 1
                    left += 1

                    key = max(has, key=has.get)
                    candidateMax = max(
                        has[key],
                        has[s[right]] + 1
                    )

        return maxLength











        #7LE HUN MSH VALID l2nu el else 
        # 3ende mfasfes 7lol lma yskr el right
        ##############################NOTES######################################3
        ##########################################################################
        # left,right=0,0
        # count=k
        # #counter={}
        # counter=0
        # max_Counter=0
        # while right<len(s) and  left<=right :
        #     if s[left]==s[right]:
        #         counter+=1
        #         right+=1
        #         max_Counter=max(max_Counter,counter)
        #     elif count>0:
        #         counter+=1
        #         right+=1
        #         count-=1
        #     else:
                
        