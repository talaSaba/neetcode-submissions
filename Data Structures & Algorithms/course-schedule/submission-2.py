class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph=defaultdict(list)
        for x,y in prerequisites:
            graph[y].append(x)
       
        def dfs(i)     :
            # if i in seen:
            #     return False
            for x in graph[i]:
                if x in seen:
                    return False
                seen.add(x)
                d=dfs(x)  
                seen.remove(x)   
                if d==False:
                    return False
                    
            return True
        for i in range(numCourses):
            seen=set()
            s=dfs(i)
            if s==False:
                return False
            #seen=set()
        return True                



        