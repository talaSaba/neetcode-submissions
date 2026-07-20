class Solution {
public:
    bool isAnagram(string s, string t) {
    if (s.length()!=t.length()){return false;}
    unordered_map<char,int>countT;
    unordered_map<char,int>countS;
    for (int i=0;i<s.length();i++)
    {
        countT[t[i]]++;
        countS[s[i]]++;


    }
    return countS==countT;
    
    
    }};