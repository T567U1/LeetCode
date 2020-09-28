class Solution(object):
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        if numRows == 0:
            list = []
            return list
        list = [[1]]
        for i in range(1, numRows):
            list1 = []
            print(i, list[i-1])
            for x in range(i + 1):
                if x == 0 or x == len(list[i-1]):
                    list1.append(1)
                    continue
                else:
                    list1.append(list[i-1][x-1] + list[i-1][x])
            list.append(list1)
        return list

c = Solution()
print(c.generate(0))
