
import pathlib as pl
import sys


def is_valid(p):
    if pl.Path(p).is_file():
        return True


def file_processing(f, mode):
        k = 0
        for i in range(1, 1000000):
            ticket = '{:06}'.format(i)
            if mode == "Moskow":
                if sum(map(int, ticket[:3])) == sum(map(int, ticket[3:])):
                        k += 1
            else:
                if sum(map(int, ticket[0::2])) == sum(map(int, ticket[1::2])):
                        k += 1
        print(f'Happy tickets for the method "{mode}" appear in file {k} time(s).')


def interactive():
        path = input("Path to file: ")
        if is_valid(path):
            f = open(path)
            mode = str(f.readline().strip())
            if mode == "Moskow" or mode == "Piter":
                file_processing(f, mode)
            else:
                print("Wrong mode.")

        else:
            print("Path was entered incorrectly.")


if __name__ == '__main__':
    values = sys.argv
    if len(values) > 1 and is_valid(values[1]):
        f = open(values[1])
        mode = str(f.readline().strip())
        if mode == "Moskow" or mode == "Piter":
            file_processing(f, mode)
        else:
            print("Wrong mode.")
    else:
        interactive()


