import pathlib as pl
import sys
instruction = '''Enter '1' if you want to count the number of occurrences
of some string in file.
Enter '2' if you want to replace one string with another
in the specified file.
    '''
hint = "You have entered an incorrect value. The mode can be a number 1 or 2!"


def is_valid(p):
    if pl.Path(p).is_file():
        return True


def file_processing(path, str_find, str_replace=None):
        if str_replace:
                f = open(path, "r+")
                s = f.read()
                f.seek(0)
                f.truncate(0)
                s = s.replace(str_find, str_replace)
                f.write(s)
                f.close()
                print("File has been modified")
        else:
                f = open(path, 'r')
                s = f.read()
                k = s.count(str_find)
                print(f'String "{str_find}" appears in file {k} time(s).')
                f.close()


def interactive():
        path = input("Path to file: ")
        if is_valid(path):
            try:
                mode = int(input(instruction))
            except ValueError:
                print(hint)
            if mode == 1:
                str_find = input("Enter string to find: ")
                file_processing(path, str_find)
            elif mode == 2:
                str_find = input("Enter string to find: ")
                str_replace = input("Enter string to replace: ")
                file_processing(path, str_find, str_replace)
            else:
                print(hint)

        else:
            print("Path was entered incorrectly.")


if __name__ == '__main__':
    values = sys.argv
    if len(values) > 2 and is_valid(values[1]):
                file_processing(*values[1:])
    else:
        interactive()
