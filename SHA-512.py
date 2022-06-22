from hashlib import sha512

string = input()
result = sha512(string.encode())
print(result.hexdigest())
