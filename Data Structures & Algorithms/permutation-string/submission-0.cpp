class Solution {
public:
    bool checkInclusion(string s1, string s2) {
        vector<int> in_s1(27);
        vector<int> in_s2(27);
        //saftey check
        if(s1.length()>s2.length()){return false;}

        //count s1;
for(int i=0;i<s1.length();i++)
{
    in_s1[s1[i]-'a']++;
}
//main loop 
int begin=0;
int end=s1.length()-1;
//initial count;
for(int i=0;i<s1.length()-1;i++)
{
    in_s2[s2[i]-'a']++;
}
while(end<s2.length())
{ in_s2[s2[end]-'a']++;
    if(in_s1==in_s2){ return true;}
    in_s2[s2[begin]-'a']--;
      begin++;
      end++;
     
}
return false;
    }
};
