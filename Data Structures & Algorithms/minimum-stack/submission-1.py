class MinStack:

    def __init__(self):
        self.mainStack=[]
        self.minStack=[]
        

    def push(self, val: int) -> None:
        self.mainStack.append(val)
        if len(self.minStack)==0:
           self.minStack.append(val) 
        else:
            mm=min(self.minStack[-1],val)
            self.minStack.append(mm)
        

    def pop(self) -> None:
        if len(self.mainStack)==0:
            return 
        self.mainStack.pop()
        self.minStack.pop()

        

    def top(self) -> int:
        if len(self.mainStack)==0:
            return 0 
        return self.mainStack[-1]
        

    def getMin(self) -> int:
        return self.minStack[-1]
        
