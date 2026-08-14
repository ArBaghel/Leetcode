class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s1,t1=sorted(s),sorted(t)
        return s1==t1
        