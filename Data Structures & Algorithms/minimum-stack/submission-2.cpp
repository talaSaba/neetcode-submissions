class MinStack {
    private:
     stack<int> st;
     stack<int> mitn;
public: 
    MinStack() {
    
       
    }
    
    void push(int val) {
        st.push(val);
        if( mitn.size()==0)
        {mitn.push(val);
return ;

        }
 else{
    int mi=min(val,mitn.top());
    mitn.push(mi);
    return;
 }  
    }
    
    void pop() {
        mitn.pop();
        st.pop();
     
 
       

    }
    
    int top() {
        return st.top();
    }
    
    int getMin() {
        return mitn.top();
        
        
    }
};
