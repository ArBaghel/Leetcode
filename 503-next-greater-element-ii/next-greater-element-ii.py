class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        st=[]
        nums+=nums
        ans=[0]*len(nums)
        for i in range (len(nums)-1,-1,-1):
            while len(st)>0 and st[-1]<=nums[i]:st.pop()
            if len(st)==0:ans[i]=-1
            else : ans [i]=st[-1]
            st.append(nums[i])  

        return ans[:len(ans)//2]      