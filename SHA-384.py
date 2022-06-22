from hashlib import sha384

string = input()
result = sha384(string.encode())
print(result.hexdigest())
