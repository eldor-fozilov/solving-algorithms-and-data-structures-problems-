# O(n) time | O(n) space - where n is the length of the array

def largestRange(array):
    longest_range = []
    longest_length = 0
    nums = {}
    for num in array:
        nums[num] = True
    for num in array:
        if not nums[num]:
            continue
        nums[num] = False
        current_length = 1
        left = num - 1
        right = num + 1
        while left in nums:
            nums[left] = False
            current_length += 1
            left -= 1
        while right in nums:
            nums[right] = False
            current_length += 1
            right += 1
        if current_length > longest_length:
            longest_length = current_length
            longest_range = [left + 1, right - 1]
    return longest_range
    
