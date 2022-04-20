home_score = list(map(int, input().split()))
away_score = list(map(int, input().split()))

home_score[0] *= 6
away_score[0] *= 6

home_score[1] *= 3
away_score[1] *= 3

home_score[2] *= 2
away_score[2] *= 2

home_score[4] *= 2
away_score[4] *= 2

print(sum(home_score), sum(away_score))