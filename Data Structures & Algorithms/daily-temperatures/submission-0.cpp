class Solution {
public:
    vector<int> dailyTemperatures(vector<int>& temperatures) {
        int n = temperatures.size();
        vector<int> res(n, 0);
        std::stack<int> st; // stores indices with temps in strictly decreasing order

        for (int i = 0; i < n; ++i) {
            // Resolve all previous days that are cooler than today
            while (!st.empty() && temperatures[i] > temperatures[st.top()]) {
                int j = st.top(); st.pop();
                res[j] = i - j;
            }
            st.push(i);
        }
        return res; // remaining indices have no warmer future day => 0
    }
};
