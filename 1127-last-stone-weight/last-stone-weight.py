class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        heap=[]
        for i in stones:
            heapq.heappush(heap,-i)
        while len(heap)>1:
            a,b=-heapq.heappop(heap),-heapq.heappop(heap)
            diff=a-b
            if diff!=0:
                heapq.heappush(heap,-diff)
        return -heap[0] if heap else 0        