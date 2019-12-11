import random
from berlekamp.register_manual import Register
from berlekamp.tools import Printer, gen_string_from_seq, reverse, gen_seq_from_int, convert_values_to_int
from berlekamp.berlekamp_manual import berlekamp_massey_manual
from berlekamp.berlekamp_copypasted import berlekamp_massey_algorithm


def main(p, sequence, skip, analyze_len, checks):

    register = Register(sequence)
    p.print("Регистр создан: {}".format(gen_string_from_seq(register.get_cc())))

    p.print("Пропускаем начальный выход: {}".format(gen_string_from_seq(register.get_next_seq(skip))))

    analyze_seq = register.get_next_seq(analyze_len)
    p.print("Взламываем на следующих данных: {}".format(gen_string_from_seq(analyze_seq)))

    hack_seq = convert_values_to_int(berlekamp_massey_manual(analyze_seq))
    p.print("Получили результат: {}".format(gen_string_from_seq(hack_seq)))

    shift = len(hack_seq) - 1

    # Эта штука на самом деле ни на что не влияет в регистре (согласно его алгоритму), но нужна для верной инициализации регистра сидом
    hack_seq.append(1)

    # Инициализация второго регистра
    hack_register = Register(hack_seq, analyze_seq)

    # Догоняем основный регистр
    p.print("Создаём новый регистр и пропускаем его начальный выход для синхронизации с основным регистром: {}".format(gen_string_from_seq(hack_register.get_next_seq(shift))))

    # Выводим сравнение данных регистров
    p.print("######################")
    p.print(hack_register.get_cc())
    p.print(register.get_cc())
    p.print("######################")
    p.print(hack_register.get_reg())
    p.print(register.get_reg())

    # Тестируем регистры (если вдруг регистры разные)
    for i in range(checks):
        original = register.get_next()
        copy = hack_register.get_next()
        if original != copy:
            p.print("Провал сравнения на шаге {}: {} != {}".format(i, original, copy))
            return False

    p.print("Всё замечательно")
    return True


if __name__ == "__main__":
    # Принтер
    p = Printer(no_print=False)

    # Чиселка или битовая последовательность
    sequence = [0, 1, 1, 0, 0, 1, 0, 0]
    sequence = gen_seq_from_int(221, 255)

    # Сколько пропускаем тактов регистра
    skip = 146

    # Длина анализируемой последовательности (надо L * 2)
    analyze_len = 16

    # Число сверок регистров
    checks = 1638400

    main(p, sequence, skip, analyze_len, checks)


