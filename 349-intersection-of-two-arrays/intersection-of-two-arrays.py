class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        #return list(set(nums1)&set(nums2))
        set1,set2=set(nums1),set(nums2)
        return list(set1.intersection(set2))
        