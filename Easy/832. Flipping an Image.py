class Solution:
    def flipAndInvertImage(self, A: List[List[int]]) -> List[List[int]]:
        return_list = []
        for i in A:
            to_add =[]
            for j in i[::-1]:
                if j:
                    to_add.append(0)
                else:
                    to_add.append(1)
            return_list.append(to_add)
        return return_list
