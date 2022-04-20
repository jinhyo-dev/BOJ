# A, B, V = map(int, input().split())
# day = 0
# total = 0
# while True:
#   day += 1
#   total += A
#   if total >= V:
#     break
#   total -= B
# print(day)
import math
A, B, V = map(int, input().split())
crawl = math.ceil((V-B) / (A-B))
print(crawl)
