"""
# Employee info
class Employee:
    def __init__(self, id: int, importance: int, subordinates: List[int]):
        # It's the unique id of each node.
        # unique id of this employee
        self.id = id
        # the importance value of this employee
        self.importance = importance
        # the id of direct subordinates
        self.subordinates = subordinates
"""
class Solution:
    def getImportance(self, employees: List['Employee'], id: int) -> int:
        dic = {}
        for i in range(len(employees)):
            dic[employees[i].id] = i

        subordinates_ = employees[dic[id]].subordinates
        sum_importance = employees[dic[id]].importance
        temp_table = [id]
        while subordinates_:
            temp_id = subordinates_.pop()
            if temp_id in temp_table:
                continue
            temp_table.append(temp_id)
            print(temp_id)
            sum_importance += employees[dic[temp_id]].importance
            if employees[dic[temp_id]].subordinates:
                for i in employees[dic[temp_id]].subordinates:
                    subordinates_.append(i)

        return sum_importance
