class Solution:
    def findMin(self, nums: List[int]) -> int:
        left, right = 0, len(nums) -1
        if nums[left] < nums[right]:
            return nums[left]
        while right - left >1:
            midVal = nums[(left+right)//2]
            leftVal = nums[left]
            rightVal = nums[right]

            if midVal > leftVal:
                left = (left+right)//2
            if midVal < rightVal:
                right = (left+right)//2

        return nums[right]
        
