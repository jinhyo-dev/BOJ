# for _ in range(int(input())):
#   cent = int(input())
#   Quarter = Dime = Nickel = Penny = 0
#   while cent > 0:
#     if cent >= 25:
#       cent -= 25
#       Quarter += 1
#       continue
#     elif cent >= 10:
#       cent -= 10
#       Dime += 1
#       continue
#     elif cent >= 5:
#       cent -= 5
#       Nickel += 1
#       continue
#     elif cent >= 1:
#       cent -= 1
#       Penny += 1
#       continue
#   print(Quarter, Dime, Nickel, Penny)

for _ in range(int(input())):
	N = int(input())
	print(N//25, (N%25)//10, ((N%25)%10)//5, N%5)