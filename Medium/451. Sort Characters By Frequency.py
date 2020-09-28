class Solution:
    def frequencySort(self, s: str) -> str:
        dic = { i: s.count(i) for i in set(s)}
        ans = sorted(dic, key = dic.get)
        ans = [i * dic[i] for i in ans]
        return ''.join(ans[::-1])
