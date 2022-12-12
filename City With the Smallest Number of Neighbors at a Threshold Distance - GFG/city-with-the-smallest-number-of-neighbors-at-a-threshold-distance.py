#User function Template for python3

from typing import List
class Solution:
    def findCity(self, n : int, m : int, edges : List[List[int]], distanceThreshold : int) -> int:
        # code here
        dist = [[float('inf') for i in range(n)]for j in range(n)]
        for elem in edges:
            dist[elem[0]][elem[1]]=elem[2]
            dist[elem[1]][elem[0]]=elem[2]
        
        for i in range(n):
            dist[i][i]=0
        
        for k in range(n):
            for i in range(n):
                for j in range(n):
                    dist[i][j]= min(dist[i][j], dist[i][k]+dist[k][j])
        
        cntcities = n
        cityNo=-1
        for city in range(n):
            cnt=0
            for adjcity in range(n):
                if dist[city][adjcity]<=distanceThreshold:
                    cnt+=1
            if cnt<=cntcities:
                cntcities=cnt
                cityNo=city
        return cityNo


#{ 
 # Driver Code Starts
#Initial Template for Python 3


if __name__=="__main__":
    T = int(input())
    for t in range(T):
        
        n, m = map(int, input().strip().split())
        edges = []
        for i in range(m):
            u, v, wt = map(int, input().strip().split())
            edges.append([u, v, wt])
        distanceThreshold = int(input())
        obj = Solution()
        ans = obj.findCity(n, m, edges, distanceThreshold)
        print(ans)
            

# } Driver Code Ends