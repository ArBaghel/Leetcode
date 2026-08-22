class Solution:
    def canPlaceFlowers(self, fb: List[int], n: int) -> bool:
        # f=l=0
        # mx=0
        # for i in range (len(fb)):
        #     if fb[i]==0:continue
        #     elif fb[i]==1:
        #         l=f=i
        #     else :l=i
        # if f==0:
        #     mx=len(fb)//2
        # else:
        #     s=f
        #     e=len(fb)-1-l
        #     mx=s//2
        #     mx+=e//2
        # c=0
        # for i in range(len(fb)):
        #     if fb[i]==0:c+=1
        #     else:
        #         mx+=(c-1)//2
        #         c=0
        # mx+=(c-1)//2
        s='0'+''.join(map(str,fb))+'0'
        return sum((len(x)-1)//2 for x in s.split('1'))>=n
    
        # return len(fb)<=mx
        