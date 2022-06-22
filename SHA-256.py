from hashlib import sha256

string = input()
result = sha256(string.encode())
print(result.hexdigest())
