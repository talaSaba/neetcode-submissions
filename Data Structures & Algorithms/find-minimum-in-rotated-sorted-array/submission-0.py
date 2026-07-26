class Solution:
    def findMin(self, nums: List[int]) -> int:
        left=0
        right=len(nums)-1
        while left<right:
            middle=(left+right)//2
            if (nums[left]<=nums[middle]<=nums[right]): #regular binary search
                right=middle-1
            else:
                if nums[left]>nums[middle]:
                    right=middle
                else:
                    left=middle+1
        return nums[left]