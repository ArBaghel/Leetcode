class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        pivot=-1
        for i in range(len(nums)-2,-1,-1):
            if nums[i]<nums[i+1]:
                pivot =i
                break
        if pivot ==-1:
            return nums.reverse()
        for i in range (len(nums)-1,-1,-1):
            if nums[i]>nums[pivot]:
                nums[i],nums[pivot]=nums[pivot],nums[i]
                break
        nums[pivot+1:]=reversed(nums[pivot+1:])
            


#   class Solution {
# public:
#     void nextPermutation(vector<int>& nums) {

#         int n = nums.size();

#         // Find pivot
#         int pivot = -1;
#         for (int i = n - 2; i >= 0; i--) {
#             if (nums[i] < nums[i + 1]) {
#                 pivot = i;
#                 break;
#             }
#         }

#         // If no pivot, reverse entire array
#         if (pivot == -1) {
#             reverse(nums.begin(), nums.end());
#             return;
#         }

#         // Find next greater element
#         for (int i = n - 1; i > pivot; i--) {
#             if (nums[i] > nums[pivot]) {
#                 swap(nums[i], nums[pivot]);
#                 break;
#             }
#         }

#         // Reverse remaining part
#         reverse(nums.begin() + pivot + 1, nums.end());
#     }
# };