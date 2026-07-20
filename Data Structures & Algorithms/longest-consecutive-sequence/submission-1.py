class Solution:
  
    def longestConsecutive(self, nums: List[int]) -> int:
        has = set(nums)
        seen = {}
        maxx = 0

        def get_length(num):
            if num in seen:
                return seen[num]

            if num - 1 not in has:
                seen[num] = 1
            else:
                seen[num] = 1 + get_length(num - 1)

            return seen[num]

        for i in range(len(nums)):
            length = get_length(nums[i])
            maxx = max(maxx, length)

        return maxx

        return maxx



        