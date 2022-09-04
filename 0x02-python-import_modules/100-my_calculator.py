#!/usr/bin/python3
from sys import argv, exit
from calculator_1 import add, sub, div, mul


def calculation():
    if __name__ == "__main__":
        if len(argv) != 4:
            print("Usage: ./100-my_calculator.py <a> <operator> <b>")
            exit(1)

        ops = {'+': add, '-': sub, '/': div, '*': mul}

        if argv[2] not in ops.keys():
            print("Unknown operator. Available operators: +, -, * and /")
            exit(1)

        a = int(argv[1])
        b = int(argv[3])
        op = argv[2]

        print("{:d} {:s} {:d} = {:d}".format(a, op, b, ops[op](a, b)))


calculation()
