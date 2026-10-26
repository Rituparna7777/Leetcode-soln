class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
     found ={}
     for index,num in enumerate(nums) :
        comp=target-num
        if comp in found :
            return [found[comp], index]
        found[num]=index
        