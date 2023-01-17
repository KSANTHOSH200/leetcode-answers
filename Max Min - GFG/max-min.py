class Solution:
    def findSum(self,A,N): 
        #code here
        min=float('inf')
        max=float('-inf')
        if N==1:
            return A[0]*2
        for i in range(N):
            if A[i]<min:
                min=A[i]
            if A[i]>max:
                max=A[i]
        return min+max



#{ 
 # Driver Code Starts
#Initial Template for Python 3



t=int(input())
for _ in range(0,t):
    n=int(input())
    a=list(map(int,input().split()))
    ob = Solution()
    print(ob.findSum(a,n))
# } Driver Code Ends