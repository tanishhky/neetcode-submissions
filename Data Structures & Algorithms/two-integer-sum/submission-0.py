class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        prevMap={}
        for i,n in enumerate(nums):
            diff=target-n
            if diff in prevMap:
                return [prevMap[diff],i]
            prevMap[n]=i

        print(hashMap)
        # comp=[]
        # n=len(nums)
        # for i range(1,n+1):
        #     compliment=target-nums[i]
        #     if compliment
        #     comp.append()