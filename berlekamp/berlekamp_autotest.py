from berlecamp2 import main
from berlekamp.tools import Printer, gen_seq_from_int

if __name__ == "__main__":
    good = 0
    bad = 0
    p = Printer(no_print=True)
    for i in range(256):
        res = main(p, gen_seq_from_int(i, 255), skip=100, analyze_len=16, checks=16384)
        if res:
            good += 1
        else:
            bad += 1
        print(i, res)
    print("###################")
    print("OK", good)
    print("ERR", bad)