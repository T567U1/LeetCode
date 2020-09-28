from datetime import date as dt
class Solution:
    def daysBetweenDates(self, date1: str, date2: str) -> int:
        date1 = date1.split('-')
        date2 = date2.split('-')
        one = dt(int(date1[0]), int(date1[1]), int(date1[2]))
        two = dt(int(date2[0]), int(date2[1]), int(date2[2]))
        ans = two - one
        return abs(ans.days)
