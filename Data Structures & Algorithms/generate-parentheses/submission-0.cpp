class Solution {
public:
    vector<string> generateParenthesis(int n) {
        vector<string> ans;
        string cur;
        cur.reserve(2 * n);
        backtrack(0, 0, n, cur, ans);
        return ans;
    }

private:
    void backtrack(int open, int close, int n, string& cur, vector<string>& ans) {
        if ((int)cur.size() == 2 * n) {     // built a full string
            ans.push_back(cur);
            return;
        }
        if (open < n) {                      // place '(' if we still can
            cur.push_back('(');
            backtrack(open + 1, close, n, cur, ans);
            cur.pop_back();
        }
        if (close < open) {                  // place ')' only if valid
            cur.push_back(')');
            backtrack(open, close + 1, n, cur, ans);
            cur.pop_back();
        }
    }
};