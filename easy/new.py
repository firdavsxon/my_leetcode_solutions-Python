def concatenationsSum(a):
    res = []
    d = {}
    for num in a:
        d[num] = num

    for j in range(len(a)):
        y=0
        if a[j] in d:
            y = d.get(a[j])
        x = a[j]
        while y>0:
            x *=10
            y//=10
        x = x + a[j]
        res.append(x)

    return sum(res)


print(concatenationsSum(a=[10, 2]))