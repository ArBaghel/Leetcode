class Solution:
    def findRestaurant(self, list1: list[str], list2: list[str]) -> list[str]:
        index1={v:i for i,v in enumerate(list1)}
        common={v:i+index1[v] for i,v in enumerate(list2) if v in index1}
        min_val=min(common.values())
        return [k for k,s in common.items() if s == min_val]



