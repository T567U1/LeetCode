class Solution:
    def removeCoveredIntervals(self, intervals: List[List[int]]) -> int:
        ans = intervals[:]
        for i, (x, y) in enumerate(intervals):
            i = 0

            while i < len(ans):
                x1, y1 = ans[i]

                if [x1, y1] == [x, y]:
                    i += 1
                    continue
                elif x1 <= x and y1 >= y:
                    ans.remove([x, y])
                    break

                i += 1

        return len(ans)
#come back to this when you have the drive
'''
class Solution:
    def removeCoveredIntervals(self, intervals: List[List[int]]) -> int:


        intervals.sort(key=lambda x: (x[0],-x[1]))

        count=0

        prev_end=0

        for _,end in intervals:

            if end > prev_end:

                count+=1
                prev_end=end
        return count
'''
