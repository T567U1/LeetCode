import math
class Solution:
    def bestCoordinate(self, towers: List[List[int]], radius: int) -> List[int]:
        r_t = {}
        for x, y, q in towers:
            key = f'{x},{y}'
            r_t[key] = []
            for x1, y1, q1 in towers:
                e = math.dist((x, y), (x1, y1))
                if e <= radius:
                    r_t[key] += [x1, y1, q1, e],

        ans = {}
        for key in r_t:
            quality = 0
            for x, y, q, e in r_t[key]:
                quality += int(q / (1 + e))

            if quality in ans:
                ans[quality] += [key],
            else:
                ans[quality] = [[key]]

        carry = 'ZZZZZZZZZZ'
        for key in ans[max(ans)]:
            x, y = key[0].split(',')
            x, y = '{0:02}'.format(int(x)), '{0:02}'.format(int(x))
            s = x + y
            if s < carry:
                carry = s
                n = [key[0]]

        return n
            
