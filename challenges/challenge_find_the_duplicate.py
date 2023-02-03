def find_duplicate(nums):
    nums.sort()

    for i in range(len(nums) - 1):
        if (not nums or not isinstance(nums[i], int) or nums[i] < 0):
            return False

        if nums[i] == nums[i + 1]:
            return nums[i]

    return False
