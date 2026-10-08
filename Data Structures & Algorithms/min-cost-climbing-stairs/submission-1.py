# Recursion BF
class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:

        if len(cost) <=1:
            return 0

        

        subPbm_1 = self.minCostClimbingStairs(cost[1:]) # choosing this subproblem, results in cost of cost[0]
        subPbm_2 = self.minCostClimbingStairs(cost[2:]) # choosing this subproblem, results in cost of cost[1]

        return min(subPbm_1+cost[0],subPbm_2 + cost[1])



        