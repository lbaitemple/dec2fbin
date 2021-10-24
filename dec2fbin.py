from getconv import getconv
import numbers


class dec2fbin:
    num=0
    sign=0
    fbin = ''
    exponent = 0
    mantissa = ''

    def __init__(self, num):

        if isinstance(num, numbers.Number):
            self.num = float(num)
            self.sign = 0 if self.num > 0 else  1
            self.mantissa, self.exponent, self.fbin =getconv(self.num)
        else:
            try:
                fl = float(num)
                self.num = fl
                self.sign = 0 if self.num > 0  else 1
                self.mantissa, self.exponent, self.fbin =getconv(fl)
            except ValueError as err:
                print('floatErr;',err)
    
    def __str__(self):
        return "%s float presentation is: %s, mantissa: %s, exponent: %s and sign: %s" %(self.num, self.fbin, self.mantissa, self.exponent, self.sign)
