class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dif_dict = {}
        for i in range(len(nums)):
            difference = target - nums[i]
            if difference in dif_dict.keys():
                return [dif_dict[difference], i]
            else:
                dif_dict[nums[i]] = i