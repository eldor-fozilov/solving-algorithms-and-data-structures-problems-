# O(n) time | O(n) space - n is the number of elements in the array

def zeroSumSubarray(nums):

    sums = set()

    if len(nums) == 0:
        return False
    
    total_sum = 0
    sums.add(total_sum)
    
    for num in nums:
        total_sum += num
        if total_sum in sums:
            return True
        else:
            sums.add(total_sum)
    
    return False
