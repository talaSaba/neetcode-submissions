class Solution {
public:
    int longestConsecutive(vector<int>& nums) {
        unordered_set<int> set;
        unordered_map<int,int> hash;   // length of the run that each value belongs to
        unordered_set<int> seen;       // marks numbers we've already assigned to a run
        int best = 0;

        // fill the set
        for (int v : nums) set.insert(v);

        // walk each distinct value once
        for (auto it = set.begin(); it != set.end(); ++it) {
            int x = *it;
            if (seen.count(x)) continue;

            // expand to full consecutive component around x
            int l = x, r = x;
            while (set.count(l - 1)) --l;
            while (set.count(r + 1)) ++r;

            int len = r - l + 1;
            best = max(best, len);

            // mark all numbers in this component as seen and store their length
            for (int v = l; v <= r; ++v) {
                seen.insert(v);
                hash[v] = len;
            }
        }

        // (optional) if you want to return from hash scanning instead:
        // int best2 = 0; for (auto& [k, v] : hash) best2 = max(best2, v); return best2;

        return best;
    }
};