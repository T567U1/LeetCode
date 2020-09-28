class Solution:
    def isPathCrossing(self, path: str) -> bool:
        position = [0,0]
        move = {'N' : (1, 0), 'S' : (-1, 0), 'E' : (0, 1), 'W' : (0, -1)}
        ans = [[0,0]]
        for i in path:
            position[0] += move[i][0]
            position[1] += move[i][1]
            if position in ans:
                return True
            ans.append([position[0], position[1]])
        return False
            
