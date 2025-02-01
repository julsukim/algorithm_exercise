import sys
from itertools import permutations

N = int(input())
group = [list(map(int, sys.stdin.readline().split())) for i in range(N)]

min_diff = 10000


def calculate_score(team):
    score = 0
    pairs = permutations(team, 2)
    for pair in pairs:
        score += group[pair[0]][pair[1]]
    return score


def recur(i, team1, team2, score1, score2):
    global min_diff
    if i >= N:
        min_diff = min(min_diff, abs(score1 - score2))
        return

    if len(team1) < N//2 and len(team2) < N//2:
        team1.append(i)
        recur(i+1, team1, team2, calculate_score(team1), score2)
        team1.pop()
        team2.append(i)
        recur(i+1, team1, team2, score1, calculate_score(team2))
        team2.pop()
    elif len(team1) < N//2:
        team1.append(i)
        recur(i+1, team1, team2, calculate_score(team1), score2)
        team1.pop()
    else:
        team2.append(i)
        recur(i+1, team1, team2, score1, calculate_score(team2))
        team2.pop()


recur(0, [], [], 0, 0)
print(min_diff)
