#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    a1 = 0
    a2 = 0
    b1 = 0
    b2 = 0
    for i in range(2):
        for j in range(2):
            a1 = tuple_a[0] if len(tuple_a) >= 1 else 0
            a2 = tuple_a[1] if len(tuple_a) > 1 else 0
            b1 = tuple_b[0] if len(tuple_b) >= 1 else 0
            b2 = tuple_b[1] if len(tuple_b) > 1 else 0
    return (a1 + b1, a2 + b2)
