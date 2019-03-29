
import pathlib as pl
import sys


def is_valid(p):
    if pl.Path(p).is_file():
        return True


def file_processing(path):
        k = 0
        f = open(path)
        mode = str(f.readline().strip())
        if mode == "Piter" or mode == "Moskow":
            for i in range(0, 1000000):
                ticket = '{:06}'.format(i)
                if mode == "Moskow":
                    if sum(map(int, ticket[:3])) == sum(map(int, ticket[3:])):
                            k += 1
                elif mode == "Piter":
                    if sum(map(int, ticket[0::2])) == sum(map(int, ticket[1::2])):
                            k += 1
        else:
            print("Wrong mode.")
        print(f'Happy tickets for the method "{mode}" appear {k} time(s).')


def interactive():
        path = input("Path to file: ")
        if is_valid(path):
                file_processing(path)
        else:
            print("Path was entered incorrectly.")


if __name__ == '__main__':
    values = sys.argv
    if len(values) > 1 and is_valid(values[1]):
        file_processing(values[1])        
    else:
        interactive()


