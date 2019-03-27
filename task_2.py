"""
@author: Rozlyvan Anastasiia, Dp-158 Python

"""
import sys
import argparse
from decimal import Decimal


def create_parser():
    parser = argparse.ArgumentParser(prog = 'task_2',
                                     description ='This program checks if you can put one envelope in another.',
                                     usage = 'Enter the sides of the envelopes.',
                                     epilog ='(c) Rozlyvan Anastasiia, Dp-158 Python')
    parser.add_argument("--a",  type = float, help = 'positive float number')
    parser.add_argument("--b",  type = float, help = 'positive float number')
    parser.add_argument("--c",  type = float, help = 'positive float number')
    parser.add_argument("--d",  type = float, help = 'positive float number')
    return parser


class Envelopes:
    def __init__(self, a, b, c, d):
        if a > 0 and b > 0 and c > 0 and d > 0:
            self.a = a
            self.b = b
            self.c = c
            self.d = d
        else:
            print("Sides must be positive and greater than zero.")
            raise ValueError
            
    def compare(self):
        
        
        if (self.a < self.c and self.b < self.d)or (self.b < self.c and self.a < self.d):
            print("You can put first envelope into second. ")
        elif(self.c < self.a and self.d < self.b) or (self.c < self.b and self.d < self.a):
            print("You can put second envelope into first. ")
        else:
            print("You can not put one envelope into another. ")


if __name__ == "__main__":
    try:
        parser = create_parser()
        values = parser.parse_args(sys.argv[1:])
        Envelopes(values.a, values.b, values.c, values.d).compare()
    except:
        while True:
            try:
                a = Decimal(input("Enter the side of the first envelope.  a = "))
                b = Decimal(input("Enter the side of the first envelope.  b = "))
                c = Decimal(input("Enter the side of the second envelope. c = "))
                d = Decimal(input("Enter the side of the second envelope. d = "))
                Envelopes(a, b, c, d).compare()
            except:
                print('Incorrect parameters !')
            ans = input('If you want to continue, type "yes" or "y": ')
            if ans.lower() != "yes" and ans.lower() != "y":
                break
