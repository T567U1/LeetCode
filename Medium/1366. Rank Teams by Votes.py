class Solution:
    def rankTeams(self, votes: List[str]) -> str:
        dic = {i : [0] * len(votes[0])  + [i] for i in votes[0]}
        for vote in votes:
            for i, v in enumerate(vote):
                dic[v][i] -= 1

        return ''.join(sorted(dic, key = dic.get))
        
