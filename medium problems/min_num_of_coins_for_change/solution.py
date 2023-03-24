# O(nd) time | O(n) space - n is the target number and
# d is the length of the "denoms" array

def minNumberOfCoinsForChange(n, denoms):
    min_number_of_coins = [float('inf') for i in range(n+1)]
    min_number_of_coins[0] = 0
    for denom in denoms:
        for amount in range(1, n+1):
            if denom <= amount:
                temp = 1 + min_number_of_coins[amount - denom]
                if temp < min_number_of_coins[amount]:
                    min_number_of_coins[amount] = temp
    min_num = min_number_of_coins[n]
    return min_num if min_num != float('inf') else -1
