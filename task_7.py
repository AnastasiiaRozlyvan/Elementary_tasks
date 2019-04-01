# !/usr/bin/env python3
"""
@author: Rozlyvan Anastasiia Dp 158 Py
"""
import sys


class Sequence:

    def __init__(self, end_of_seq):
        self.end_of_seq = end_of_seq

    def get(self):
        numb = 1
        while numb**2 < self.end_of_seq:
            yield numb
            numb += 1

    def print_sequence(self):
        is_first = True
        for i in self.get():
            if is_first:
                print(i, end="")
                is_first = False
            else:
                print(f', {i}', end="")


def params_assigned(end_num):
    try:
        if int(end_num) > 0:
            Sequence(int(end_num)).print_sequence()
            print()
            return True
        else:
            raise ValueError
    except ValueError:
            print("You have entered an incorrect value.")
            return False


def main():

    arg = sys.argv
    if len(arg) <= 1 or not params_assigned(arg[1]):
        while True:
            end_num = input("Enter the boundary of sequence: ")
            if params_assigned(end_num):
                break


if __name__ == "__main__":
    main()

