import heapq
class Solution:

    def nthUglyNumber(self, n: int) -> int:
        # l1=[]
        # i=1
        # while True:
        #     x=i
        #     for p in [2,3,5]:
        #         while x%p==0: 
        #             x//=p
        #     if x==1: l1.append(i)
        #     if len(l1)==n: 
        #         return i
        #     i+=1
        heap=[1]
        seen={1}
        for i in range (n):
            ugly=heapq.heappop(heap)
            for p in [2,3,5]:
                nxt=ugly*p
                if nxt not in seen:
                    seen.add(nxt)
                    heapq.heappush(heap,nxt)
        return ugly


    
