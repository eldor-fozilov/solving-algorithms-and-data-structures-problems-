# O(n) time | O(n) space - where n is the length of the input array

def missingNumbers(nums):
    nums = set(nums)
    missing_numbers = []
    for num in range(1, len(nums) + 3):
        if num not in nums:
            missing_numbers.append(num)
    return missing_numbers