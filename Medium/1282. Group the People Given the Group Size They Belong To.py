class Solution:
    def groupThePeople(self, groupSizes: List[int]) -> List[List[int]]:
        ans = {}
        for i in range(len(groupSizes)):
            if groupSizes[i] in ans:
                if len(ans[groupSizes[i]][-1]) = groupSizes[i]:
                    ans[groupSizes[i]].append([i])
                else:
                    ans[groupSizes[i]][-1].append(i)
            else:
                ans[groupSizes[i]] = [[i]]

        dic = []
        for i in ans:
            for j in ans[i]:
                dic.append(j)

        return dic
