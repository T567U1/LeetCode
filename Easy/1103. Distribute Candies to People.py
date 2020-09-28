class Solution:
    def distributeCandies(self, candies: int, num_people: int) -> List[int]:
        if num_people == 1:
            return [candies]
        p = [0] * num_people
        i, c, l = 0, 1, len(p)
        while candies > c:
            if i == l:
                i = 0
            p[i] += c
            candies -= c
            c += 1
            i += 1

        if i <= l - 1:
            p[i] += candies
        else:
            p[0] += candies

        return p
