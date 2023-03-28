# Average: O(n^2) time | O(n^2) space
# Worst: O(n^3) time | O(n^2) space - where n is the length of the input array

def fourNumberSum(array, target_sum):
    quadruplets = []
    pair_sums_dict = {}
    for i in range(1, len(array) - 1):
        for j in range(i+1, len(array)):
            current_sum = array[i] + array[j]
            if (target_sum - current_sum) in pair_sums_dict:
                for pair in pair_sums_dict[target_sum - current_sum]:
                    quadruplets.append(pair + [array[i], array[j]])
        for k in range(0,i):
            current_sum = array[i] + array[k]
            if current_sum not in pair_sums_dict:
                pair_sums_dict[current_sum] = [[array[k], array[i]]]
            else:
                pair_sums_dict[current_sum].append([array[k], array[i]])
    return quadruplets
