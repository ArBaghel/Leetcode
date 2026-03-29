class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        # if needle in haystack:
        #     return haystack.index(needle)
        # return -1
        for i in range (len(haystack)):
            if haystack[i:i+len(needle)]==needle:
                return i
        return -1
        # if not needle: return 0
        # lps=[0]*len(needle)
        # length,i=0,1
        # while i < len(needle):
        #     if needle[i] == needle [length]:
        #         length += 1
        #         lps [i] = length
        #         i += 1
        #     else:
        #         if length != 0:
        #             length = lps[length - 1]   
        #         else:
        #             lps[i] = 0
        #             i += 1
        # i=j=0
        # while i < len(haystack):
        #     if haystack[i] == needle[j]:
        #         i  += 1
        #         j += 1
        #     if j ==len(needle):
        #         return i-j
        #     elif i < len(haystack) and haystack [i] != needle[j]:
        #         if j != 0:
        #             j=lps[j-1]
        #         else :
        #             i+=1
        # return -1

