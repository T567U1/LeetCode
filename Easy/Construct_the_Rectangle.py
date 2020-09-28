class Solution:
    def constructRectangle(self, area: int):
        for i in range(int(area ** (1/2)), 0, -1):
            print(i)
            if area % i == 0:
                return [area // i, i]



c = Solution()
for i in range(10):
    print(c.constructRectangle(i))
