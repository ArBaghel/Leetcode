class Solution:
    def combinationSum2(self, candidate: list[int], target: int) -> list[list[int]]:
        res=[]
        candidate.sort()
        def backtrack(s,path,total):
            if total==target:
                res.append(path[:])
                return
            if total>target:
                return
            for i in range (s,len(candidate)):
                if i>s and candidate[i]==candidate[i-1]:continue
                path.append(candidate[i])
                backtrack(i+1,path,total+candidate[i])
                path.pop()
        backtrack(0,[],0)
        return res
        