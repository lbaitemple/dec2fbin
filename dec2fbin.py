from getconv import getconv
import numbers


class dec2fbin:
    fbin = ''
    exponent = 0
    mantissa = ''

    def __init__(self, num):
        if isinstance(num, numbers.Number):
            self.mantissa, self.exponent, self.fbin =getconv(float(num))
        else:
            try:
                fl = float(num)
                self.mantissa, self.exponent, self.fbin =getconv(fl)
            except ValueError as err:
                print('floatErr;',err)

