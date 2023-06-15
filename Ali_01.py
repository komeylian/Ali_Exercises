
a = 10
b = 10


def masahat(tol=10, arz=10):
    s = tol*arz
    print('tol = ', tol, ' | arz = ', arz, '| Masahat = ', s)


def mohit(tol=10, arz=10):
    M = (tol + arz)*2
    print('tol = ', tol, ' | arz = ', arz, '| Mohit   = ', M)


#masahat(2, 30)

#mohit(arz=10, tol=20)

print("\n\n\n")
a = str({'BTC': {'USDT': 25728.2}})
b = a[2:-2]
c = b[0:3]

d = b[8:12]
f = b[14:22]

print(type(a), a)


print("\n\n", b)

print("\n\n", c, d, f)

print(len(a))


for bbb in range(len(a)):
    print(bbb, a[bbb])


print(a[2:5], a[10:14], a[17:24])
