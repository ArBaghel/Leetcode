class Solution:
    def combinationSum(self, candidate: list[int], target: int) -> list[list[int]]:
        res=[]
        def backtrack(s,path,total):
            if total==target:
                res.append(path[:])
                return
            if total>target:
                return
            for i in range (s,len(candidate)):
                path.append(candidate[i])
                backtrack(i,path,total+candidate[i])
                path.pop()
        backtrack(0,[],0)
        return res
        