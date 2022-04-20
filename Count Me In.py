vowels = ['a', 'e', 'i', 'o', 'u']
for _ in range(int(input())):
  numOfVowels = 0
  numOfConsonants = 0 
  str = input()
  for word in str:
    if word.lower() in vowels:
      numOfVowels += 1
    elif word != ' ':
      numOfConsonants += 1
  print(numOfConsonants, numOfVowels)