# класс LFSR
class Register:
    def __init__(self, cc, reg=None):
        # можно задать сид, но если сида нет, он равен коэффициентам функции обратной связи
        self.cc = cc.copy()
        if reg is not None:
            self.reg = reg.copy()[len(reg)-len(self.cc):]
        else:
            self.reg = self.cc.copy()
        self.length = len(self.cc)

    def get_next(self):
        # итерация регистра
        res = self.reg[-1]
        f = 0
        for i, n in enumerate(self.reg[:-1]):
            f += n * self.cc[i]

        del self.reg[self.length-1]
        self.reg.insert(0, f % 2)
        return res

    def get_cc(self):
        return self.cc

    def get_reg(self):
        return self.reg

    def get_next_seq(self, length=1):
        # если надо сразу несколько итераций и вернуть всё в последовательности
        res = []
        for _ in range(length):
            res.append(self.get_next())
        return res
