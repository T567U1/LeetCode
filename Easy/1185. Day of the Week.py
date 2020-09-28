import datetime
class Solution:
    def dayOfTheWeek(self, day: int, month: int, year: int) -> str:

            week_days= ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday','Sunday']
            l = [day, month, year ]
            day = datetime.date(l[2],l[1],l[0]).weekday()

            return week_days[day]
