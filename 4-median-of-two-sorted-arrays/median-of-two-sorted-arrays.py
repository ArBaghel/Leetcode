class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
     merg=sorted(nums1+nums2)
     n=len(merg)
     if n %2==1:
        return float(merg[n // 2])
     else:
        return (merg[n // 2 - 1] + merg[n//2]) / 2.0