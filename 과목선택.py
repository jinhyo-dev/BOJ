A_scores = [int(input()) for _ in range(4)]
B_scores = [int(input()) for _ in range(2)]
A_scores.sort(reverse=True)
total = [A_scores[i] for i in range(3)]
total.append(max(B_scores))
print(sum(total))