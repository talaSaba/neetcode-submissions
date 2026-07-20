from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # answers=[]
        # dict=defaultdict(list)
        # for s in strs:
        #     x=s
        #     d="".join(sorted(s))
        #     dict[d].append(x)
        # for key, values in dict.items():
        #     answers.append(values)

        # return answers    
        answers=[]
        d=defaultdict(list)
        for i in strs:
            j=i
            s=list(j)
            key=s.sort()
            ss= "".join(s)
            d[ss].append(i)
        for  key in d.keys():
            answers.append(d[key])
        return answers    

        