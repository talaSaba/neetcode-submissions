class Solution {
public:
    int lengthOfLongestSubstring(string s) {
        unordered_set<char> seen;
        int begin=0,end=0;
        int count=0,best=0;
        while(end<s.size())
        {
             while (seen.count(s[end])) {
                seen.erase(s[begin]);
                ++begin;
                --count;
            }
            // Now it's safe to include s[end]
            seen.insert(s[end]);
            ++count;
            best = std::max(best, count);
            ++end;
            
        }
        
   return best; }
};
