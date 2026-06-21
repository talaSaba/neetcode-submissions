#include <bits/stdc++.h>
using namespace std;

class Solution {
public:
    string minWindow(string s, string t) {
        unordered_map<char,int> s1Count; // need
        unordered_map<char,int> s2Count; // have

        for (int i = 0; i < (int)t.length(); i++) {
            s1Count[t[i]]++;
        }

        int required = (int)s1Count.size(); // distinct chars we must satisfy
        int formed = 0;                     // how many are currently satisfied

        int begin = 0, end = 0;
        int bestLen = INT_MAX, bestStart = 0;

        while (end < (int)s.length()) {
            char c = s[end];
            if (s1Count.count(c)) {
                s2Count[c]++;
                if (s2Count[c] == s1Count[c]) formed++; // just satisfied this char
            }

            // While window is valid, try to shrink from the left
            while (formed == required) {

                // Skip over non-required chars OR surplus required chars
                while (begin <= end &&
                       (!s1Count.count(s[begin]) || s2Count[s[begin]] > s1Count[s[begin]])) {
                    if (s1Count.count(s[begin])) {
                        s2Count[s[begin]]--; // dropping a surplus unit is safe
                    }
                    begin++;
                }

                // Now s[begin] is essential; record current best window
                if (end - begin + 1 < bestLen) {
                    bestLen = end - begin + 1;
                    bestStart = begin;
                }

                // Drop the essential char to move on (this will break validity)
                if (s1Count.count(s[begin])) {
                    s2Count[s[begin]]--;
                    if (s2Count[s[begin]] < s1Count[s[begin]]) formed--;
                }
                begin++;
            }

            end++;
        }

        return bestLen == INT_MAX ? "" : s.substr(bestStart, bestLen);
    }
};
