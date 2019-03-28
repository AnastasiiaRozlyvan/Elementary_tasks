#!/usr/bin/env python3
"""
@author: Rozlyvan Anastasiia Dp 158 Py
"""
import sys


def params_assigned(num):
    try:
        if 9999 > int(num) > 0:
            print(num_to_words(int(num)))
            return True
        else:
            raise ValueError
    except ValueError:
            print("You have entered an incorrect value.")
            return False


def num_to_words(num):

    words = {0: 'zero', 1: 'one', 2: 'two', 3: 'three', 4: 'four', 5: 'five',
             6: 'six', 7: 'seven', 8: 'eight', 9: 'nine', 10: 'ten',
             11: 'eleven', 12: 'twelve', 13: 'thirteen', 14: 'fourteen',
             15: 'fifteen', 16: 'sixteen', 17: 'seventeen', 18: 'eighteen',
             19: 'nineteen', 20: 'twenty',
             30: 'thirty', 40: 'fourth', 50: 'fifty', 60: 'sixty',
             70: 'seventy', 80: 'eighty', 90: 'ninety'}

    if num < 20:
        return words[num]

    if num < 100:
        if num % 10 == 0:
            return words[num]
        else:
            return words[num//10 * 10] + ' ' + words[num % 10]
    k = 1000
    m = k * 1000

    if num < k:
        if num % 100 == 0:
            return words[num//100] + ' hundred'
        else:
            return words[num//100] + ' hundred ' + num_to_words(num % 100)
    if num < m:
        if num % k == 0:
            return num_to_words(num//k) + ' thousand'
        else:
            return num_to_words(num//k) + ' thousand, ' + num_to_words(num % k)


def main():

    arg = sys.argv
    if len(arg) <= 1 or not params_assigned(arg[1]):
        while True:
            num = input('Please enter an integer between 1 and 9999: ')
            if params_assigned(num):
                break


if __name__ == "__main__":
    main()
