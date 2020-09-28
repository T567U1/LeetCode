#good luck!
class Solution:
    def shortestToChar(self, S: str, C: str) -> List[int]:
        return_array = []
        for i in range(len(S)):
            if C in S[i::-1]:
                if C in S[i::-1] and C not in S[i:]:
                    return_array.append(S[i::-1].index(C))
                    continue
                elif S[i::-1].index(C) < S[i:].index(C):
                    return_array.append(S[i::-1].index(C))
                    continue
            return_array.append(S[i:].index(C))

        return return_array
