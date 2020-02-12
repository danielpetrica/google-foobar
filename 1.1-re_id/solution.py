def answer(n):
    numList = ""
    num = 2
    while numList.__len__() <= n + 5:  # don't generate a huge 10000 character string from prime numbers each time, you need less.
        if is_prime(num):
            numList += num.__str__()
            #print(num)
        num += 1

    b = n + 5
    return numList[n:b]


def is_prime(n):
    if n == 2 or n == 3: return True
    if n < 2 or n % 2 == 0: return False
    if n < 9: return True
    if n % 3 == 0: return False
    r = int(n ** 0.5)
    f = 5
    while f <= r:
        # print '\t', f
        if n % f == 0: return False
        if n % (f + 2) == 0: return False
        f += 6
    return True


print(answer(0)) # aded for debug, you can change 0 with any number
