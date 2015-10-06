def plural(n, forms):
    if n % 10 == 1 and n % 100 != 11:
        return forms[0]
    elif 2 <= n % 10 <= 4 and (12 > n % 100 or n % 100 > 14):
        return forms[1]
    else:
        return forms[2]


words = {"утюг": ["утюг", "утюга", "утюгов"],
         "ложка": ["ложка", "ложки", "ложек"],
         "гармошка": ["гармошка", "гармошки", "гармошек"],
         "чайник": ["чайник", "чайника", "чайников"]}

thing = input()
number = int(input())
print(" ".join((str(number), plural(number, words[thing]))))
