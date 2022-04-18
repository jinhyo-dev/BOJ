books = []
dic = dict()
arr = []
for _ in range(int(input())):
  book = input()
  books.append(book)

for i in list(set(books)):
  dic[i] = books.count(i)

for k in dic.keys():
  if dic[k] == max(dic.values()):
    arr.append(k)

arr.sort()
print(arr[0])