# O(nlog(n) + mlog(m)) time | O(1) space, n is the length of the first input array
# and m is the length of the second input array

from math import inf
def smallestDifference(arrayOne, arrayTwo):

    arrayOne.sort()
    arrayTwo.sort()

    min_pair = [inf, None, None]

    left = 0
    for i in range(len(arrayOne)):
        
        current_distance = None
        right = len(arrayTwo)
        while left <= right:
            mid = (left + right) // 2
            current_distance = abs(arrayTwo[mid] - arrayOne[i])
            
            neighbor_distance_left, neighbor_distance_right = None, None
            
            if mid > 0:
                neighbor_distance_left = abs(arrayTwo[mid-1] - arrayOne[i])
            if mid < len(arrayTwo) - 1:
                neighbor_distance_right = abs(arrayTwo[mid+1] - arrayOne[i])

            if neighbor_distance_left is not None and neighbor_distance_left < current_distance:
                right = mid - 1
            elif neighbor_distance_right is not None and neighbor_distance_right < current_distance:
                left = mid + 1
            else:
                left = mid
                break

        if current_distance < min_pair[0]:
            min_pair = [current_distance, i, mid]
            
    return [arrayOne[min_pair[1]], arrayTwo[min_pair[2]]]
