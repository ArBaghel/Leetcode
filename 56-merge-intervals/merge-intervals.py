class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key=lambda x:x[0])
        m=[]
        prev=0
        for i in range (1,len(intervals)):
            if intervals[i][0] <= intervals[prev][1]:
                intervals[prev][1]=max(intervals[i][1],intervals[prev][1])
            else:
                m.append(intervals[prev])

                prev=i
        m.append(intervals[prev])
        return m