class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        keys = [0]
        visited = {}
        in_ = 0
        while len(visited) < len(rooms):
            if not keys:
                return False
                break
            in_ = keys.pop()
            if in_ in visited:
                continue
            else:
                keys.extend(rooms[in_])
                visited[in_] = 1
        return True
