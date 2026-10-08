class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        a = [0, 0, 0]
        for n in nums:
            a[n] +=1
        
        res = []
        for i, n in enumerate(a):
            res += [i] * n
        nums[:] = res