def factorize(n):
    q = 2
    if n % q == 0:
        p = n / q
    elif n % q != 0:
        q += 1
        p = n / q
        print(str(n) + "=" + str(int(p)) + "*" + str(int(q)))
        return ''
