def factors(n):
    q = int(2)
    while q < n:
        if n % q == 0:
            p = int (n / q)
            print(str(n) + "=" + str(p) + "*" + str(q))
    return''
with open("tests/test00", "r") as f:
    n = print(f.read())
print(factors(18))
