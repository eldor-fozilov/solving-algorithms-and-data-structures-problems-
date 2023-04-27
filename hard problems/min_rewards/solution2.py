# O(n) time | O(n) space - where n is the length of the "scores" input array

def minRewards(scores):

    rewards = [1 for score in scores]
    for i in range(1, len(scores)):
        if scores[i] > scores[i-1]:
            rewards[i] = rewards[i-1] + 1
    for i in reversed(range(len(scores) - 1)):
        if scores[i] > scores[i+1]:
            rewards[i] = max(rewards[i], rewards[i+1] + 1)
    return sum(rewards)
