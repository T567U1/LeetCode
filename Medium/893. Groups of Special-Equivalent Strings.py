#since our only option are between odd and evens we
#don't have to overcomplicate
class Solution:
    def numSpecialEquivGroups(self, A: List[str]) -> int:
        dic = {}
        for word in A:
            temp = ''.join(sorted(word[::2])) + ''.join(sorted(word[1::2]))
            dic[temp] = 1
        return len(dic)

    #one liner:
    return len(set([''.join(sorted(i[::2])) + ''.join(sorted(i[1::2])) for i in A]))
