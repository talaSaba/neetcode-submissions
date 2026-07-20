class Solution {
public:
    vector<int> topKFrequent(vector<int>& nums, int k) {

 vector<int> out;
 unordered_map<int,int> c;
 for(int i=0;i<nums.size();i++)
 {c[nums[i]]++; }
int maxf=-1;
for(auto & [key,val]: c){ maxf=max(val,maxf);}
 vector<vector<int>> freq(maxf+1);
 for(auto & [key,val]: c){ freq[val].push_back(key);}
  for (int f = maxf; f >= 1 && (int)out.size() < k; --f) {
    for( auto& j: freq[f]){
        out.push_back(j);
        if ((int)out.size() == k) break;
    }
  }


return out;};

};
