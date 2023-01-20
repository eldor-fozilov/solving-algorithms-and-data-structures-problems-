# Brute-force solution

# Time Complexity: k*n*(2^n), where k is the sum of the coins (too big!)
# Space Complexity: n*(2^n)

def generate_subset(arr_coins, index, subset, subsets):
    if index == len(arr_coins):
        subsets.append(subset.copy())
    else:
        generate_subset(arr_coins, index + 1, subset + [arr_coins[index]], subsets)
        generate_subset(arr_coins, index + 1, subset, subsets)
    
def get_power_set(coins):
    subsets = []
    subset = []
    initial_index = 0
    generate_subset(coins, initial_index, subset, subsets)
    return subsets


def check(candidate_num, coins):

    power_set = get_power_set(coins)
    for subset in power_set:
        if candidate_num == sum(subset):
                return False
    return True
    

def nonConstructibleChange(coins):

    if len(coins) == 0:
        return 1

    coins_sum = sum(coins)
    
    for candidate_num in range(1, coins_sum):
        if candidate_num not in coins:
            check_equality = check(candidate_num, coins)
            if check_equality:
                return candidate_num
    
    return  coins_sum + 1
