class Solution:

    def __init__(self, radius: float, x_center: float, y_center: float):
        self.circle = (radius, x_center, y_center)

    def randPoint(self) -> List[float]:
        # random angle
        alpha = 2 * math.pi * random.random()
        # random radius
        r = self.circle[0] * math.sqrt(random.random())
        # calculating coordinates
        x = r * math.cos(alpha) + self.circle[1]
        y = r * math.sin(alpha) + self.circle[2]
        return [x, y]
#https://stackoverflow.com/questions/30564015/how-to-generate-random-points-in-a-circular-distribution

# Your Solution object will be instantiated and called as such:
# obj = Solution(radius, x_center, y_center)
# param_1 = obj.randPoint()
