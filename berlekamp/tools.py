import math


class Printer:
    def __init__(self, no_print):
        self.no_print = no_print

    def print(self, data):
        if not self.no_print:
            print(data)


def gen_seq_from_int(number, max_=0):
    max_ = max(number, max_)
    seq = [0 for _ in range(int(math.ceil(math.log2(max_ + 1))))]
    i = 0
    while number > 0:
        seq[i] = number & 1
        number = number >> 1
        i += 1
    return seq


def convert_values_to_int(seq):
    return [int(n) for n in seq]


def gen_string_from_seq(seq):
    str_ = ''
    for n in convert_values_to_int(seq):
        str_ += str(n)
    return str_


def reverse(l):
    res = []
    for i in range(len(l)):
        res.append(l[len(l) - 1 - i])
    return res
