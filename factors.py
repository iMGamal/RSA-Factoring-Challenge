def factors(n):
    for q in range(2, n):
        p = int(n / q)
        if n % q == 0:
            print(str(n) + "=" + str(p) + "*" + str(q))
            break
    return''
print(factors(9999))
