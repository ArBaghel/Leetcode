class Solution:
    def thirdMax(self, nums: list[int]) -> int:
        fir=sec=thr=None
        for n in nums:
            if n==fir or n==sec or n== thr:continue
            if fir is None or n>fir:
                fir,sec,thr=n,fir,sec
            elif sec is None or n>sec:
                sec,thr=n,sec
            elif thr is None or n>thr:
                thr=n
        return thr if thr is not None else fir
    

        