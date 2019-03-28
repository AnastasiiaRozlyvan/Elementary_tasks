"""
@author: Rozlyvan Anastasiia, Dp-158 Python

"""
import sys
import argparse
from math import ceil, floor


def create_parser():
    parser = argparse.ArgumentParser(prog = 'task1',
                                     description = '''This program prints a chessboard. Enter the height and width (positive integers).''',
                                     epilog ='''(c) Rozlyvan Anastasiia, Dp-158 Python''')
    parser.add_argument("--height", default = 0, type = int, help = 'positive integer')
    parser.add_argument("--width", default = 0, type = int, help = 'positive integer')
    return parser



def chess(h = None, w = None):
        try:
            if not w and not h:
                h = int(input("Enter height :"))
                w = int(input("Enter width :"))
            if w < 0 or h < 0 or type(w) != int or type(h) != int:
                print("Arguments must be positive !")
            else:
                for i in range(h):
                    if i % 2 == 0:
                        print(ceil(w / 2) * "* ")
                    else:
                        print(floor(w / 2) * " *")
        except:
            print('Incorrect parameters !')


if __name__ == "__main__":
    try:
        parser = create_parser()
        values = parser.parse_args(sys.argv[1:])
        chess(values.width, values.height)
    except ValueError:
        chess()