multi10 = []
numeros1000 = []

for i in range(0,1000000):
    oi = i * 10
    multi10.insert(0,oi)

for i in range(0,1000000):
    numeros1000.insert(0,i)

a = list(set(numeros1000).difference(set(multi10).intersection(numeros1000)))

for i in range (0, 1000000):
    if (a[i] + int(str(a[i])[::-1])) % 2 == 1 and a[i] + int(str(a[i])[::-1]) < 1000000:
        print("número n:", a[i], "número reverso(n):",int(str(a[i])[::-1]),"soma:", a[i] + int(str(a[i])[::-1]))