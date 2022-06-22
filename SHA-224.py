from hashlib import sha224

string = input()
result = sha224(string.encode())
print(result.hexdigest())
