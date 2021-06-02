"""
Given an integer array nums, find the contiguous subarray (containing at least
one number) which has the largest sum and return its sum.
https://leetcode.com/problems/maximum-subarray/
"""


def brute_force(nums):
    """A brute force solution to maximum subarray problem."""
    if len(nums) == 1:
        return nums[0]
    max_sum = []
    for index in range(len(nums)):
        local_sum = 0
        for j in range(index, len(nums)):
            local_sum += nums[j]
            max_sum.append(local_sum)
    return max(max_sum)


def two_pointers(nums):
    """A two pointers solution to maximum subarray problem."""
    if len(nums) == 1:
        return nums[0]
    cur_sum = sum(nums)
    max_sum = []
    left = 0
    right = len(nums) - 1

    def find_max(left, right, sum):
        if right - left >= 0:
            max_sum.append(sum)
        else:
            return 0
        find_max(left + 1, right, sum - nums[left])
        find_max(left, right - 1, sum - nums[right])

    find_max(left, right, cur_sum)
    return max(max_sum)


def kadane(nums):
    """A dynamic programming approach to maximum subarray problem."""
    size = len(nums)
    if not size:
        return 0

    if size == 1:
        return nums[0]

    local_max = nums[0]
    global_max = nums[0]

    for i in range(1, size):
        local_max = max(nums[i], nums[i] + local_max)
        global_max = max(global_max, local_max)
    return global_max


def optimized_kadane(nums):
    """An optimized kadane approach to maximum subarray problem."""
    global_max = nums[0]
    curr = nums[0]
    for num in nums[1:]:
        if curr < 0:
            curr = num
        else:
            curr += num
        global_max = max(global_max, curr)
    return global_max


def divide_and_conquer(nums):
    """A divide and conquer approach to maximum subarray problem."""

    def find_cross_sum(nums, low, mid, high):
        left_sum = nums[mid]
        sum = 0
        for i in range(mid, low - 1, -1):
            sum = sum + nums[i]
            if sum > left_sum:
                left_sum = sum
        right_sum = nums[mid + 1]
        sum = 0
        for i in range(mid + 1, high + 1):
            sum = sum + nums[i]
            if sum > right_sum:
                right_sum = sum
        return left_sum + right_sum

    def find_sub(nums, low, high):
        if high == low:
            return nums[low]
        else:
            mid = (low + high) / 2
            left_sum = find_sub(nums, low, mid)
            right_sum = find_sub(nums, mid + 1, high)
            cross_sum = find_cross_sum(nums, low, mid, high)
        return max(left_sum, right_sum, cross_sum)

    return find_sub(nums, 0, len(nums) - 1)
