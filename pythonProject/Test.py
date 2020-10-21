i = 1
j = 1
k = 1
ar = []


for a in range(i+1):
    print('a value',a)
    print(ar)
    for b in range(j+1):
        print('b value',b)
        print(ar)
        for c in range(k+1):
            print('c value',c)
            ar.append([a,b,c])
            print(ar)

print(ar)

