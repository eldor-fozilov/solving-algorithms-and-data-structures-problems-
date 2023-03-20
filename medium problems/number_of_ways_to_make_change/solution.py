# O(nd) time | O(n) space - n is the target number and
# d is the length of the "denoms" array

def numberOfWaysToMakeChange(n, denoms):
    ways = [0 for i in range(n+1)]
    ways[0] = 1
    for denom in denoms:
        for amount in range(1, n+1):
            if denom <= amount:
                ways[amount] += ways[amount - denom]
    return ways[n]
