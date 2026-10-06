class Solution:
    def findRestaurant(self, list1: list[str], list2: list[str]) -> list[str]:
        index1={value:i for i, value in enumerate(list1)}
        common_val={value:i+index1[value] for i,value in enumerate(list2) if value in index1}
        min_value=min(common_val.values())
        return [val for val,v in common_val.items() if v==min_value]
