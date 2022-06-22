from hashlib import sha1

string = input()
result = sha1(string.encode())
print(result.hexdigest())
