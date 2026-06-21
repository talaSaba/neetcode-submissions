class Solution {
public:
    vector<vector<string>> groupAnagrams(vector<string>& strs) {
     vector<vector<string>> out;
     unordered_map<string,std::vector<int>> res;
     unordered_map<string,std::vector<string>>s;
     for(int i=0;i<strs.size();i++)
     {
        std::vector<int>c{0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0};
        for(int j=0;j<strs[i].size();j++)
        {
            c[strs[i][j]-'a']++;
        }
        bool flag=false;
        string k="";
        for (auto& [key, group] : res) {
            if(c==group)
            {flag=true;
            k=key;
            break;}
    //out.push_back(group);
}
if(!flag){
 res[strs[i]]={c};
 s[strs[i]]={strs[i]};

     }
     else{s[k].push_back(strs[i]);

     }}
 for (auto& [key, group] : s) {
    out.push_back(group);
}
    
return out;
    }
};
