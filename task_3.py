"""
@author: Rozlyvan Anastasiia, Dp-158 Python
"""
import argparse
import sys


def create_parser():
    parser = argparse.ArgumentParser(prog='task_3',
                                     description='This program sorts triangles.',
                                     usage='Enter name and lengthes of sides.',
                                     epilog='(c) Rozlyvan Anastasiia, Dp-158 Python')

    return parser

class Triangle:
    def __init__(self, name, a, b, c):
        if (a < c + b and c < b + a and b < c + a
                and a > 0 and b > 0 and c > 0):
                    self.valid = True
                    self.name = name.lower()
                    self.a = a
                    self.b = b
                    self.c = c
        else:
            self.valid = False

    def area(self):
        s = (self.a + self.b + self.c)/2
        return (s*(s - self.a)*(s - self.b)*(s - self.c))**0.5


if __name__ == "__main__":
    triangles_list = []
    parser = create_parser()
    values = parser.parse_args(sys.argv[1:])
    while True:
        try:
                name, a, b, c = input("Enter name, side a, side b, side c: ").split()
                t = Triangle(name, float(a), float(b), float(c))
                if t.valid:
                    triangles_list.append(t)
                else:
                    print("Invalid triangle.")
        except ValueError:
            print("The sides of the triangle are entered incorrectly!")
        if triangles_list:
            print("============= Triangles list: ===============")
            triangles_list.sort(key=lambda t: t.area(), reverse=True)
            for i, t in enumerate(triangles_list):
                print(f'{i+1}. [Triangle {t.name}]: {round(t.area(), 2)} cm')
        else:
            print("So far, the list of triangles is empty.")
        ans = input('If you want to continue, type "yes" or "y": ').strip().lower()
        if ans != "yes" and ans != "y":
                break
