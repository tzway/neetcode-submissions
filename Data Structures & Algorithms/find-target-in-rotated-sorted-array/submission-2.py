class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) - 1

        while l <= r:
            m = (l + r) // 2
            if nums[m] == target:
                return m
            
            # mid 在起始点左侧
            if nums[l] <= nums[m]:
                if nums[l] <= target < nums[m]:
                    r = m - 1
                else:
                    l = m + 1
            # mid 在起始点右侧
            else:
                if nums[m] < target <=nums[r]:
                    l = m + 1
                else:
                    r = m - 1
        

        return -1
