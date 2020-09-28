class Solution:
    def displayTable(self, orders: List[List[str]]) -> List[List[str]]:
        menu = []
        index = 1
        for i in orders:
            if i[-1] not in menu:
                menu.append(i[-1])

        menu = sorted(menu)
        menu = {i: menu.index(i) + 1  for i in menu}
        ans = [['Table'] + list(menu.keys())]
        tables = {}

        for ord_ in orders:
            if ord_[1] in tables:
                tables[ord_[1]][menu[ord_[-1]]] = str(int(tables[ord_[1]][menu[ord_[-1]]]) + 1)
            else:
                tables[ord_[1]] = [ord_[1]] + ['0'] * len(menu)
                tables[ord_[1]][menu[ord_[-1]]] = str(int(tables[ord_[1]][menu[ord_[-1]]]) + 1)

        tables = {int(i): tables[i] for i in tables}

        ans = ans + [tables[i] for i in sorted(tables)]

        return ans
        
