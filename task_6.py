
import pathlib as pl
import sys


def is_valid(p):
    if pl.Path(p).is_file():
        return True

def file_processing(f, mode):
        s = f.readlines()
        s = ''.join(s[1:]).split('\n')
        if mode == "Moskow":
                k = 0
                for numb in s:
                    first_sum = 0
                    last_sum = 0
                    for symbol in numb[:3]:
                        first_sum += int(symbol)
                    for symbol in numb[3:]:
                        last_sum += int(symbol)
                    if first_sum == last_sum:
                        k+=1
        else:
            k = 0
            for numb in s:
                even_sum = 0
                odd_sum = 0
                for i in range(0, 6):
                    if i % 2 == 0:
                        even_sum += int(numb[i])
                    else:
                        odd_sum += int(numb[i])

                if even_sum == odd_sum:
                    k += 1
        f.close()
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
                file_processing(values[1])
    else:
        interactive()


