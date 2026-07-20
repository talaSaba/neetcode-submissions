class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:

        def check(capacity):
            used_days = 1
            curr = 0

            for w in weights:
                if curr + w <= capacity:
                    curr += w
                else:
                    used_days += 1
                    curr = w

            return used_days <= days

        left = max(weights)
        right = sum(weights)
        ans = right

        while left <= right:
            mid = (left + right) // 2

            if check(mid):
                ans = mid
                right = mid - 1
            else:
                left = mid + 1

        return ans