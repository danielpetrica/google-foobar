#!/usr/bin/python
# -*- coding: UTF-8
def solution(n):
    count = 0
    current_stack = n
    if (n == 0):
        return 1
    if (n == 2):
        return 1
    if (n == 3):
        return 2

    while current_stack != 1:
        count += 1
        if is_even(current_stack):
            # divido per 2
            current_stack = current_stack / 2
            # print(f"divido per due {current_stack}")
        else:
            current_stack = choose_add_sub(current_stack)
        # print(f"{n}->{current_stack}")

    return count

    # # print(count)
    # print(f"current_stack  {n}  {count}")


# ** determina se un numero è pari
def is_even(n):
    return (n % 2) == 0


def choose_add_sub(m):
    _sott = solution((m - 1) / 2)
    _add = solution((m + 1) / 2)
    if _sott < _add:
        # print(f"sottraggo 1")
        return (m - 1)
    else:
        # print(f"aggiungo 1")
        return (m + 1)


n = 0

while n < 100:
    print(n,solution(n))
    n = n + 1
