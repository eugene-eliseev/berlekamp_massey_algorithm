from berlekamp2 import main
from berlekamp.tools import Printer, gen_seq_from_int

BITS = 8  # длина регистра
SKIP = 84  # кол-во пропускаемых тактов вначале

if __name__ == "__main__":
    iterations = 2 ** BITS
    checks = 2 ** (BITS * 2)
    good = 0
    bad = 0
    p = Printer(no_print=True)
    progress = 0
    goods = []
    for i in range(iterations):
        res = main(p, gen_seq_from_int(i, iterations-1), skip=SKIP, analyze_len=16, checks=checks)
        if res:
            good += 1
            goods.append(i)
        else:
            bad += 1
        if int(100*i/iterations) != progress:
            progress = int(100*i/iterations)
            print("Прогресс: {} %".format(progress))
    print("###################")
    print("OK", good)
    print("ERR", bad)
    print("###################")
    print("Число итераций проверок каждого регистра:",checks)
    print("Эффективность:",round(good/(good+bad), 3))
    print("Угаданные регистры:", goods)
