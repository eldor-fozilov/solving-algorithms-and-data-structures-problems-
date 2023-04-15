# O(n) time | O(1) space - where n is the length of the input array

def missingNumbers(nums):
    total_sum = (len(nums)+2)*(len(nums) + 3) // 2
    nums_sum = sum(nums)
    difference = total_sum - nums_sum
    mean_of_missing_values = difference // 2

    left_sum = right_sum = 0
    for i in range(1, len(nums) + 3):
        if i <= mean_of_missing_values:
            left_sum += i
        else:
            right_sum += i

    sub_left_sum = sub_right_sum = 0
    for num in nums:
        if num <= mean_of_missing_values:
            sub_left_sum += num
        else:
            sub_right_sum += num
    missing_val1 = left_sum - sub_left_sum
    missing_val2 = right_sum - sub_right_sum
    return [missing_val1, missing_val2]
    
