
interval = (-50, 50)

for x1 in range(*interval):
    print(x1)
    for x2 in range(*interval):
        if x1 == x2:
            continue
        a = x1 + x2
        b = x1*x2
        for x3 in range(*interval):
            x4 = a - x3
            for x5 in range(*interval):
                x6 = a - x5
                if x3 * x4 == b - x1 and x5 * x6 == b - x2:
                    print(x1, x2, x3, x4, x5, x6, '', a, b)
