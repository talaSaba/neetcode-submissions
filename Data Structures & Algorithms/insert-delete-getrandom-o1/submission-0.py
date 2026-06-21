class RandomizedSet:

    def __init__(self):
        self.numMap={}# the hashMap keys : values values : indexes in the array 
        self.nums=[]

        

    def insert(self, val: int) -> bool:
        if val in self.numMap:
            return False
        self.numMap[val]=len(self.nums)
        self.nums.append(val)
        return True
        

    def remove(self, val: int) -> bool:
        if val not in self.numMap:
            return False
        # i want to swap between the indexes :
        valueToSwap=self.nums[-1]
        #self.numMap[valueToSwap]=self.numMap[val]
        temp=self.numMap[val]
        self.nums[self.numMap[val]]=self.nums[self.numMap[self.nums[-1]]]
        self.nums[-1]=val
        self.nums.pop()
        self.numMap[valueToSwap]=self.numMap[val]
        del self.numMap[val]
        return True

        

    def getRandom(self) -> int:
        return random.choice(self.nums)


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()