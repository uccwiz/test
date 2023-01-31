def split_list(l, n):
    for i in range(0, len(l), n):
        yield l[i:i + n]
l = [i+1 for i in range(10)]
print(l)
n = 3
a = list(split_list(l, n))
print(a)
