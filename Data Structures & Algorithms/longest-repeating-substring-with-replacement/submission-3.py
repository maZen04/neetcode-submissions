class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count = {}
        res = 0
        l = 0
        maxF = 0
        for r in range(len(s)):
            if s[r] in count:
                count[s[r]] += 1
            else:
                count[s[r]] = 1
            maxF = max(maxF,count[s[r]])
            if (r-l+1) - maxF>k:
                count[s[l]]-=1
                l+=1
            res = max(res,r-l+1)
        return res