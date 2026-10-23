class Solution:
    def hIndex(self, citations: list[int]) -> int:
        citations.sort(reverse=True)
        count=0
        for r,i in enumerate(citations):
            if i >=r+1:count=r+1
            else:break
        return count



        