class MinStack {
public:
   vector<int> stack;
        vector<int> minVar;
    MinStack() {
     
       
    }
    
    void push(int val) {
        stack.push_back(val);
       // endStack++;
        if(minVar.size()==0){minVar.push_back(val);
        }
        else{
            int m=std::min(minVar[minVar.size()-1],val);
            minVar.push_back(m);
           // endMinVar++;
        }
    }
    
    void pop() {
     
       stack.pop_back();
      
       minVar.pop_back();
       

    }
    
    int top() {
        return stack[stack.size()-1];
    }
    
    int getMin() {
        return minVar[minVar.size()-1];
        
    }
};
