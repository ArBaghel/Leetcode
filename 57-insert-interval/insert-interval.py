class Solution:
    def insert(self, intervals: list[list[int]], newInterval: list[int]) -> list[list[int]]:
        intervals.append(newInterval)
        intervals.sort()
        ans=[]
        for s,e in intervals:
            if not ans or s>ans[-1][1]:
                ans.append([s,e])
            else:ans[-1][1]=max(ans[-1][1],e)
        return ans