#User function Template for python3

class Solution:
    
    #Function to find sum of weights of edges of the Minimum Spanning Tree.
    def spanningTree(self, V, adj):
        #code here
        import heapq
        visited = [0]*V
        pq=[(0,0)]
        sum=0
        while len(pq)>0:
            curr_wt, curr_node = heapq.heappop(pq)
            if visited[curr_node]==1:
                continue
            visited[curr_node]=1
            sum+=curr_wt
            for elem in adj[curr_node]:
                adjNode = elem[0]
                wt = elem[1]
                if visited[adjNode]==0:
                    heapq.heappush(pq, (wt, adjNode))
        return sum


#{ 
 # Driver Code Starts
#Initial Template for Python 3
import atexit
import io
import sys

# Contributed by : Nagendra Jha

if __name__ == '__main__':
    test_cases = int(input())
    for cases in range(test_cases):
        V,E = map(int,input().strip().split())
        adj = [[] for i in range(V)]
        for i in range(E):
            u,v,w = map(int,input().strip().split())
            adj[u].append([v,w])
            adj[v].append([u,w])
        ob = Solution()
        
        print(ob.spanningTree(V,adj))
# } Driver Code Ends