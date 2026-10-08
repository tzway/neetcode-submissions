class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        res = []
        track = []
        
        def backtrack(start):
            if sum(track) == target:
                res.append(track.copy())
            
            for i in range(start, len(candidates)):
                if i > start and candidates[i] == candidates[i-1]:
                    continue
                track.append(candidates[i])
                backtrack(i+1)
                track.pop()
        backtrack(0)
        return res