class Solution:
    def minReorder(self, n: int, connections: List[List[int]]) -> int:
        ans = 0
        seem = {}
        for i in range(len(connections)):
            if 0 in connections[i]:
                if connections[i][1] != 0:
                    connections[i] = connections[i][::-1]
                    ans += 1

            elif connections[i][0] not in connections[i - 1] or connections[i][0] not in connections[i - 1]:
                if connections[i][0] in seem:
                    connections[i] = connections[i][::-1]
                    ans += 1

            elif connections[i][1] != connections[i - 1][0]:
                connections[i] = connections[i][::-1]
                ans += 1

            seem[connections[i][0]] = 1
            seem[connections[i][1]] = 1
        return ans
