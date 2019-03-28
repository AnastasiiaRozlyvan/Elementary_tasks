# !/usr/bin/env python3
"""
@author: Rozlyvan Anastasiia Dp 158 Py
"""
import sys


class Fib:

    def __init__(self, start_of_seq, end_of_seq):
        self.end_of_seq = end_of_seq
        self.start_of_seq = start_of_seq

    def get(self):
        fib1, fib2 = 0, 1
        while fib2 <= self.end_of_seq:
            fib1, fib2 = fib2, fib1 + fib2
            if fib1 >= self.start_of_seq:
                yield fib1

    def print_sequence(self):
        is_first = True
        for i in self.get():
            if is_first:
                print(i, end="")
                is_first = False
            else:
                print(f', {i}', end="")


def params_assigned(start_num, end_num):
    try:
        if int(end_num) > 0 and int(start_num) > 0:
            Fib(int(start_num), int(end_num)).print_sequence()
            print()
            return True
        else:
            raise ValueError
    except ValueError:
            print("You have entered an incorrect value.")
            return False


def main():

    arg = sys.argv
    if len(arg) <= 2 or not params_assigned(arg[1], arg[2]):
        while True:
            start_num = input("Enter the start of sequence: ")
            end_num = input("Enter the boundary of sequence: ")
            if params_assigned(start_num, end_num):
                break


if __name__ == "__main__":
    main()
