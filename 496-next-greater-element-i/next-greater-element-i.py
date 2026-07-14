class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        st=[]
        ans={}
        for i in range (len(nums2)-1,-1,-1):
            while len(st)>0 and st[-1]<nums2[i]:st.pop()
            if len(st)==0:ans[nums2[i]]=-1
            else :ans[nums2[i]]=st[-1]
            st.append (nums2[i])
        return list(map(lambda x: ans[x],nums1))
        