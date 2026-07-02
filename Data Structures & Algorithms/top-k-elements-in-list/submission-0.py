class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        ans={}
        # set_ans=set(nums)÷

        for i in nums:
            if i not in ans:
                ans[i]=1
            else:
                ans[i]+=1
        
        sorted_ans={k:v for k,v in sorted(ans.items(), key=lambda item:item[1], reverse=True)}
        return (list(sorted_ans)[0:k])