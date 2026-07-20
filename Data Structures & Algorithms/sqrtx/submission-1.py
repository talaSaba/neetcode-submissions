class Solution:
    def mySqrt(self, x: int) -> int:
        l=0
        r=x
        while l<=r:
            m=(l+r)//2
            s=m*m
            if s== x:
                return m
            elif s>x:
                r=m-1
            else:
                l=m+1
        return r

        