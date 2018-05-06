

def func(a0=1, a1=1):
    if a1 > 10 ** 6:
        return a1
    return func(a0=a1, a1=a1 + a0 + 1)


print(func())
