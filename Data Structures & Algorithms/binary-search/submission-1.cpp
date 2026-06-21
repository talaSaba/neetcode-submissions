class Solution {
public:
    int search(vector<int>& nums, int target) {
        int first=0,last=nums.size()-1;
        while(first<=last)// why =?---> because we need the last element chack
        {
           int middle=(first+last)/2;
           if(nums[middle]>target){ last=middle-1;}// also some major edge cases
           else if (nums[middle]<target){ first=middle+1;}
else {return middle;}
        }
       return -1; 
    }
};
