#재귀
def fibo(x):
    if x == 1 or x == 2:
        return 1
    return fibo(x-1) + fibo(x-2)

d = [0] * 100

def fibo2(x):
    if x == 1 or x == 2:
        return 1
    if d[x] != 0:
        return d[x]
    d[x] = fibo2(x-1) + fibo2(x-2)
    return d[x]

print(fibo2(99))