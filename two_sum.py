class solution:
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                if nums[i] + nums[j] == target:
                   return [i, j]
                else:
                    continue


test = solution()
output = test.twoSum([3, 2, 4, 8], 6)
print(output)
