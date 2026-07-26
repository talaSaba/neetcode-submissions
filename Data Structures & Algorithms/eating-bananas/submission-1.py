class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        left = 1
        right = max(piles)

        while left < right:
            middle = (left + right) // 2

            hours = 0
            for pile in piles:
                hours += (pile + middle - 1) // middle

            if hours > h:
                left = middle + 1
            else:
                right = middle

        return left