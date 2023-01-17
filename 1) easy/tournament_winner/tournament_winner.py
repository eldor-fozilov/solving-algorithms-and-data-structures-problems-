# Time Complexity: O(n), n - the number of competitions
# Space Complexity: O(k), k - the number of teams 

def tournamentWinner(competitions, results):
    # Write your code here.

    count_wins = {}
    for i in range(len(competitions)):
        winner_team = competitions[i][1 - results[i]]
        if winner_team not in count_wins:
            count_wins[winner_team] = 3
        else:
            count_wins[winner_team] += 3
    return max(count_wins, key = count_wins.get)
