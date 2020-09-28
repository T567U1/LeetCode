class Solution:
    def trap(self, height: List[int]) -> int:
        walls, traped_water = [], 0
        for i in height:
            if i > traped_water:
                traped_water = i

            
