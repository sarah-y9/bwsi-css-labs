"""
lab_1c.py

Given a list of numbers, return the maximum sum of any contiguous subarray of the list.

Do not assume anything. Account for all edge cases.

Derived from LeetCode problem: https://leetcode.com/problems/maximum-subarray/ (leetcode medium)
"""

# TODO: Find and resolve the bug in the following implementation. Create unit tests to verify your fix.
def max_subarray_sum(nums: list[int]) -> int:
    """
    Function that takes in a list of integers and returns the maximum sum of any contiguous subarray.

    Args:
        nums (list[int]): List of integers.

    Returns:
        int: The maximum sum of any contiguous subarray.
    """
    sanitize_list(nums)
    
    if not nums:
        return 0
    
    max_current = max_global = nums[0]
    
    for num in nums[1:]:
        max_current = max(num, max_current + num)
        if max_current > max_global:
            max_global = max_current
            
    return max_global

def sanitize_list(nums: list[int]) -> list[int]:
    """
    Function to sanitize input for max_subarray_sum

    Returns:
        list[int]: The list of integers.
    """
    for x in nums:
        if type(x) is not int:
            raise ValueError("Invalid input. Please enter a list of valid numbers.")
    return nums

# Example usage:
def main():
    nums = [-2,1,-3,4,-1,2,1,-5,4]
    result = max_subarray_sum(nums)
    print(f"Maximum subarray sum: {result}")

if __name__ == "__main__":
    main()