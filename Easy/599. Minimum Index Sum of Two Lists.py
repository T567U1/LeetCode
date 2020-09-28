class Solution:
    def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:
        dic = {}
        #convert both to set and find common items by using intersection
        for i in set(list1).intersection(set(list2)):
            dic[i] = list1.index(i) + list2.index(i)
        #because problem requires this get all key with values equal min
        return [i for i in dic if dic.get(i) == min(dic.values())]
