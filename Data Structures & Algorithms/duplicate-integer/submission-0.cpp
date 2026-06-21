class Solution {
public:
    bool hasDuplicate(vector<int>& nums) {
        //std::map c;
       // std::map<int, std::string> m;
       std::map <int,int> counter;
        for(int i=0;i<nums.size();i++)
        {
            auto it = counter.find(nums[i]);
         if (it != counter.end()){ return true;}
         else{
            counter[nums[i]]=1;
         }
        }
        return false;
        
    }
};