class Solution:
    def magicalString(self, n: int) -> int:
        s= "122"
        flag = "1"
        #current pointer
        ptr = 2
        while len(s) <= n:
            s += int(s[ptr]) * flag
            flag = "1" if flag == "2" else "2"
            ptr += 1

        return s[:n].count("1")
