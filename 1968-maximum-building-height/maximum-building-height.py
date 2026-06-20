class Solution:
    def maxBuilding(self, n: int, restrictions: List[List[int]]) -> int:
        restrictions +=[[1,0],[n,n-1]]
        restrictions.sort()
        for i in range (1,len(restrictions)):
            restrictions[i][1]=min(restrictions[i][1],restrictions[i-1][1]+restrictions[i][0]-restrictions[i-1][0])
        for i in range(len(restrictions)-2,-1,-1):
            restrictions[i][1] = min(restrictions[i][1], restrictions[i+1][1] + restrictions[i+1][0]-restrictions[i][0])
        return max((restrictions[i][1]+restrictions[i-1][1]+restrictions[i][0]-restrictions[i-1][0])//2 for i in range(1,len(restrictions)))