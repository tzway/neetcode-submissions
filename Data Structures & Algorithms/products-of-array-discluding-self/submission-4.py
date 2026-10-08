class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix = []
        postfix = []
        tmp = 1
        for n in nums:
            tmp *= n
            prefix.append(tmp)
        tmp = 1
        for n in reversed(nums):
            tmp *=n
            postfix.append(tmp)
        postfix = list(reversed(postfix))

        res = []
        for i in range(len(nums)):
            pre = 1
            post = 1
            if i-1 >=0:
                pre = prefix[i-1]
            if i+1 <len(nums):
                post = postfix[i+1]
            res.append(pre*post)
        return res
