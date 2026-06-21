class Solution {
public:
    int evalRPN(vector<string>& tokens) {
        std::stack<int> history;
        int i = 0;
        while (i < (int)tokens.size()) {
            const std::string& tk = tokens[i];
            if (tk == "+" || tk == "-" || tk == "*" || tk == "/") {
                if (history.size() < 2) return -1; // or throw
                int b = history.top(); history.pop();  // num2
                int a = history.top(); history.pop();  // num1

                int res = 0;//history.pop return void not number 
                if (tk == "+")      res = a + b;
                else if (tk == "-") res = a - b;
                else if (tk == "*") res = a * b;
                else                res = a / b;  // truncates toward 0

                history.push(res);
                i++;
            } else {
                int num = std::stoi(tk);          // handles "-11" etc.
                history.push(num);
                i++;
            }
        }

        // result should be the only value left
        return history.top();
    }
};
