class Solution {
public:
    bool isValid(string s) {
        std::stack<char> stack;
        for(int i=0;i<s.size();i++)
        {
            if (s[i]=='{'||s[i]=='['||s[i]=='(')
            {
                stack.push(s[i]);
            }
            else{
                if(stack.empty()){return false;}
                char last=stack.top();
                if((s[i]=='}'&&last=='{')||(s[i]==']'&&last=='[')||(s[i]==')'&&last=='('))
                { stack.pop();}
                else{ return false;}
            }
        }
        if(stack.empty()){return true;}
        return false;
        
    }
};
