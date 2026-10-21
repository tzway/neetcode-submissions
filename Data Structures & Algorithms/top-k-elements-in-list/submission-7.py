class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        ct = Counter(nums)
        return list(
            tp[0] for tp in ct.most_common(k)
        )