result = []
n = int(input('N='))
for i in range(1, n):
    for b in range(2, i):
        if (i%b == 0):
            break
    else:
        result.append(i)
print(result)
