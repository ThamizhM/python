def count(s):
    ccount = {}
    for i in s:
        if i in ccount:
            ccount[i] += 1
        else:
            ccount[i] = 1
    return ccount

n = "Hello"
result = count(n)

for i, j in result.items():
    print(f"The character '{i}' appears {j} times in the string.")
