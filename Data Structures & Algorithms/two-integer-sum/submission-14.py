class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # ans=[]
        # hash=Counter(nums)
        # for i in range(len(nums)):
        #     x=hash[(target-nums[i])];
        #     if x>0 and i!=nums.index(target-nums[i]):
        #         return sorted([i,nums.index(target-nums[i])])

        # return        []
            
        positions = defaultdict(list)

        for i, num in enumerate(nums):
            positions[num].append(i)

        for num in positions:
            needed = target - num

            if needed not in positions:
                continue

            if num != needed:
                return [positions[num][0], positions[needed][0]]

            # Example: num = 3, needed = 3
            if len(positions[num]) >= 2:
                return [positions[num][0], positions[num][1]]

        return [-1]   
