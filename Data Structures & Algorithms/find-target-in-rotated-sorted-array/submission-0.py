class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left = 0
        right = len(nums) - 1

        while left <= right:
            middle = (left + right) // 2

            if nums[middle] == target:
                return middle

            # The left range [left ... middle] is regularly sorted
            if nums[left] <= nums[middle]:

                # Is the target inside the sorted left range?
                if nums[left] <= target < nums[middle]:
                    right = middle - 1
                else:
                    left = middle + 1

            # Otherwise, the right range [middle ... right] is regularly sorted
            else:

                # Is the target inside the sorted right range?
                if nums[middle] < target <= nums[right]:
                    left = middle + 1
                else:
                    right = middle - 1

        return -1