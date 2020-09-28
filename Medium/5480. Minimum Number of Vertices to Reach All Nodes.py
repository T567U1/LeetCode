class Solution:
    def findSmallestSetOfVertices(self, n: int, edges: List[List[int]]) -> List[int]:
        nx, ny = {}, {}
        for x, y in edges:
            nx[x] = 0
            ny[y] = 0

        for i in ny:
            if i in nx:
                del nx[i]

        return list(nx.keys())



            
