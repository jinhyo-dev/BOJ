string = "How are you? I'm fine, and you?"
table = {}
for ch in string:
    if ch.isalpha():
        upper = ch.upper()
        if upper not in table:
            table[upper] = 1
        else:
            table[upper] += 1

largest = 0
largest_key = ""
for key in table:
    if largest < table[key]:
        largest = table[key]
        largest_key = key
    print(key, ":", table[key])


print(largest)
print(largest_key)
