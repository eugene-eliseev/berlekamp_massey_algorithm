import random
from berlekamp.register_manual import Register
from berlekamp.tools import Printer, gen_string_from_seq, reverse, gen_seq_from_int


def main(START_SEQ, RANDOM_GEN, RANDOM_LEN, no_print=False):
    p = Printer(no_print)

    p.print("Создаём регистр и инициализируем его. Длина: {}".format(len(START_SEQ) + 1))
    p.print(gen_string_from_seq(START_SEQ) + '1')
    register = Register(START_SEQ)

    num = random.randint(RANDOM_GEN[0], RANDOM_GEN[1])
    p.print("Пропускаем {} тактов".format(num))
    for _ in range(num):
        register.get_next()

    num = random.randint(RANDOM_LEN[0], RANDOM_LEN[1])
    p.print("Берём последовательность длины {} из регистра:".format(num))
    block_data = []
    for i in range(num):
        res = register.get_next()
        block_data.append(res)
    p.print(gen_string_from_seq(block_data))

    p.print('')
    p.print("Взламываем регистр...")
    res_algo = berlekamp_massey_algorithm(block_data)
    # res_algo = berlekamp_massey_manual(block_data)

    hack = gen_string_from_seq(res_algo)
    reg_seq = gen_string_from_seq(START_SEQ)

    p.print("Результат:")
    p.print(hack)

    p.print("Начинаем сравнение выхода регистров. 1000 итераций")
    hack_register = Register(reverse(res_algo[1:]))
    for i in range(1000):
        original = register.get_next()
        copy = hack_register.get_next()
        if original != copy:
            p.print("Провал сравнения на шаге {}: {} != {}".format(i, original, copy))
            break

    if hack == reg_seq:
        p.print("УСПЕШНЫЙ ВЗЛОМ")
        return True, None
    else:
        if len(hack) < len(reg_seq):
            hack_ = hack
            for _ in range(len(reg_seq)-len(hack)):
                hack_ += '0'
            if hack_ == reg_seq:
                p.print("УСПЕШНЫЙ ВЗЛОМ")
                return True, None
        p.print("НЕСОВПАДЕНИЕ")
        return hack, reg_seq


if __name__ == "__main__":
    # стартовая последовательность. добавится ещё один бит, равный 1
    START_SEQ = [1, 0, 1, 1, 1, 0, 1]
    START_SEQ = gen_seq_from_int(42, 127)

    # сколько пропустить тактов регистра, прежде чем начать взлом
    RANDOM_GEN = [256, 256]

    # какой длины взять последовательность для взлома
    RANDOM_LEN = [16, 16]

    # автотест
    AUTOTEST = False

    # генерация чисел для автотеста
    AUTOTEST_RANGE = [2, 255]

    if not AUTOTEST:
        main(START_SEQ, RANDOM_GEN, RANDOM_LEN)
    else:
        errors = []
        i = 0
        for n in range(AUTOTEST_RANGE[0], AUTOTEST_RANGE[1]):
            for n1 in range(RANDOM_GEN[0], RANDOM_GEN[1] + 1):
                for n2 in range(RANDOM_LEN[0], RANDOM_LEN[1] + 1):
                    r1, r2 = main(gen_seq_from_int(n), [n1, n1], [n2, n2], no_print=True)
                    if r2 is not None:
                        errors.append((n, n1, n2, r1, r2))
                    i += 1
        print("Тестов пройдено: {}".format(i))
        print("#######################")
        print("Обнаружено ошибок: {}".format(len(errors)))
        for err in errors:
            print("Ошибка", err)
