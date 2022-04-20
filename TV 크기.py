D, H, W = map(int, input().split())
R = D / (H**2 + W**2) ** 0.5
print(int(H*R), int(W*R))