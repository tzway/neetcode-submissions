class Solution:
    def search(self, nums: List[int], target: int) -> int:
        offset = self.findStart(nums)
        def ni(i):
            return (i + offset) % len(nums)
        left, right = 0, len(nums) -1

        while left <= right:
            mid = (left+right) //2 
            if nums[ni(mid)] == target:
                return ni(mid)
            if nums[ni(mid)] < target:
                left = mid + 1
            else:
                right = mid - 1 
        
        return -1

    def findStart(self, nums):
        left, right = 0, len(nums) - 1
        
        while left < right:
            mid = (left + right) // 2
            # 如果中间元素大于右边元素，最小值在右边
            if nums[mid] > nums[right]:
                left = mid + 1
            # 如果中间元素小于等于右边元素，最小值在左边
            else:
                right = mid
        return left
