class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key=lambda x:x[0])
        merged_intervals=[]
        first_interval=0
        for i in range(1,len(intervals)):
            if intervals[i][0]<=intervals[first_interval][1]:
                intervals[first_interval][1]=max(intervals[i][1],intervals[first_interval][1])
            else:
                merged_intervals.append(intervals[first_interval])
                first_interval=i
        merged_intervals.append(intervals[first_interval])
        return merged_intervals



