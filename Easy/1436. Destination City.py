class Solution:
    def destCity(self, paths: List[List[str]]) -> str:
        set_, set1 = set(), set()
        for i in paths:
            set_.add(i[0])
            set1.add(i[1])

        return set1.difference(set_).pop()
