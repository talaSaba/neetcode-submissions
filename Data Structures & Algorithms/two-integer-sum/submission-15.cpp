class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        std::unordered_map<int,int> reverse_array;
        std::vector<int> s;
        for(int i=0;i<nums.size();i++)
        {
            reverse_array.insert({nums[i], i});
        }
        for(int i=0;i<nums.size();i++)
        {
            if(reverse_array.count(target-nums[i])&&reverse_array[target-nums[i]]!=i)
            {if(i<reverse_array[target-nums[i]])
            { s.push_back(i);
                 s.push_back(reverse_array[target-nums[i]]);
                  return s;
               
            }
            else{
                 s.push_back(reverse_array[target-nums[i]]);
                s.push_back(i);
                 return s;
            }
           }
        }
    return s;}
};
