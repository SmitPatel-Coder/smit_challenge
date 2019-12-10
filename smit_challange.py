import math
from math import pow
class Complex:
    def __init__(self, real, imag):
        self.real = real
        self.imag = imag
    def __add__(self, no):
        return Complex(self.real+no.real, self.imag+no.imag)
    def __sub__(self, no):
        return Complex(self.real-no.real, self.imag-no.imag)
    def __mul__(self, no):
        return Complex(self.real*no.real-self.imag*no.imag, self.real*no.imag+self.imag*no.real)
    def __div__(self, no):
        try: 
            return self.__mul__(Complex(no.real, -1*no.imag)).__mul__(Complex(1.0/(no.mod().real)**2, 0))
        except ZeroDivisionError as e:
            print e
            return None
    def mod(self):
        return Complex(pow(self.real**2+self.imag**2, 0.5), 0)
    def __str__(self, precision=2):
        return str(("%."+"%df"%precision)%float(self.real))+('+' if self.imag>=0 else '-')+str(("%."+"%df"%precision)%float(abs(self.imag)))+'i'


if __name__ == '__main__':
    c = map(float, raw_input().split())
    d = map(float, raw_input().split())
    x = Complex(*c)
    y = Complex(*d)
    print '\n'.join(map(str, [x+y, x-y, x*y, x/y, x.mod(), y.mod()]))