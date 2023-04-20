# O(n) time | O(n) space - where n is the length of the "scores" input array

def updateRewards(rewards, start, end, type_of_seq):
    if type_of_seq == "increasing":
        rewards[start] = 1
        for i in range(start + 1, end + 1):
            rewards[i] = rewards[i-1] + 1
    else:
        rewards[end] = 1
        for i in range(end - 1 , start - 1, -1):
            rewards[i] = rewards[i+1] + 1

def minRewards(scores):
    rewards = [0 for i in range(len(scores))]

    if len(scores) == 1:
        return 1
        
    idx = 0
    while idx < len(scores) - 1:
        start1 = end1 = idx
        while end1 < len(scores) - 1 and scores[end1] > scores[end1 + 1]:
            end1 += 1
        updateRewards(rewards, start1, end1, 'decreasing')
      
        if start1 - 1 > 0 and rewards[start1 - 1] <= rewards[start1]:
            rewards[start1 - 1] = rewards[start1] + 1
        
        start2 = end2 = end1
        while end2 < len(scores) - 1 and scores[end2] < scores[end2 + 1]:
            end2 += 1
        updateRewards(rewards, start2, end2, 'increasing')

        if end2 + 1 == len(scores) - 1 and rewards[end2 + 1] == 0:
            rewards[end2 + 1] = 1
            break
        idx = end2 + 1
        
    return sum(rewards)
