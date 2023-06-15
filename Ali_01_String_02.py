a = str({'BTC': {'USDT': 25728.2}})

b = ''
for i in range(len(a)):
    if a[i] == '}' or a[i] == '{' or a[i] == "'" or a[i] == ":":
        print(' '.ljust(2), '|', end='')

    else:
        print((a[i]).ljust(2), '|', end='')
        b += a[i]
print()
for ii in range(len(a)):
    print(str(ii).ljust(2), '|', end='')

print("\n")
print(b)
