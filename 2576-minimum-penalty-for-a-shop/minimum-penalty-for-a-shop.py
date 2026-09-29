class Solution:
    def bestClosingTime(self, customers: str) -> int:
        p=best=min_p=0
        for i,ch in enumerate(customers,1):
            p+=1 if ch=="N" else -1
            if p<min_p:
                min_p=p
                best=i
        return best
        