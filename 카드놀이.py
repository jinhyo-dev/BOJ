A_Card = list(map(int, input().split()))
B_Card = list(map(int, input().split()))
A_Score = 0
B_Score = 0
winner = ''

if A_Card == B_Card:
    print(10, 10)
    print('D')

else:
    for i in range(10):
        if A_Card[i] > B_Card[i]:
            A_Score += 3
            winner = 'A'
        elif A_Card[i] < B_Card[i]:
            B_Score += 3
            winner = 'B'
        else:
            A_Score += 1
            B_Score += 1

    print(A_Score, B_Score)
    if A_Score == B_Score:
        print(winner)
    else:
        print('A' if A_Score > B_Score else 'B')