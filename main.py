def get_nod(a, b):
    while a != b:
        if a > b:
            a -= b
        else:
            b -= a

    return a


res = get_nod(18, 24)
print(res)
