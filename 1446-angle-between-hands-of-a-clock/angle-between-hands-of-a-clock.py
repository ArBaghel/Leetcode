class Solution:
    def angleClock(self, hour: int, minutes: int) -> float:
        hourdegree= (hour % 12)*30+(0.5*minutes)
        minutedegree=(minutes*6)
        diff=abs(hourdegree-minutedegree)
        return min(diff,360-diff)