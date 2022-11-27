for _ in range(int(input())):
    string = input()
    print('yes' if len(string) <= 9 and len(string) >= 6 else 'no')