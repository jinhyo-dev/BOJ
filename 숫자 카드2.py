import sys
from collections import Counter

input = sys.stdin.readline
N = input()
card = input().split()
M = input()
num_of_cards = input().split()

C = Counter(card)
print(' '.join(f'{C[i]}' if i in C else '0' for i in num_of_cards))