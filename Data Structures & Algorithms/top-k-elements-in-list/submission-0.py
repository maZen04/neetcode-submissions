class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        h={}
        freq = [[] for i in range(len(nums)+1)]
        for i in nums:
            if i in h:
                h[i]+=1
            else:
                h[i]=1

        for num, count in h.items():
            freq[count].append(num)
        
        res=[]
        for i in range(len(freq)-1,0,-1):
            for n in freq[i]:
                res.append(n)
                if len(res)==k:
                    return res