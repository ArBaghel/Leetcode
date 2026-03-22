class Solution:
    def canJump(self, nums: List[int]) -> bool:
        # jump=0
        # for i in range (len(nums)):
        #     if i > jump :
        #         return False
        #     jump=max(jump,i+nums[i])
        # return True

        jump = nums[0] 
        for i in range(1, len(nums)):
            if jump == 0:  
                return False
            jump -=1
            jump = max(jump, nums[i])  
        return True