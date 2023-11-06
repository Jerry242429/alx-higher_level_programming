#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    tuple_len = len(tuple_a)
    tuple_lenth = len(tuple_b)

    if tuple_len == 0:
        m1 = 0
        m2 = 0
    elif tuple_len == 1:
        m1 = tuple_a[0]
        m2 = 0
    else:
        m1 = tuple_a[0]
        m2 = tuple_a[1]

    if tuple_lenth == 0:
        n1 = 0
        n2 = 0
    elif tuple_lenth == 1:
        n1 = tuple_b[0]
        n2 = 0
    else:
        n1 = tuple_b[0]
        n2 = tuple_b[1]

    new = (m1 + n1, m2 + n2)

    return (new)
