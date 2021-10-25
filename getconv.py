# ‐*‐ encoding: utf‐8 ‐*‐
#!/usr/bin/python python ‐tt
# .11101 => .90625
# ff_dec2bin(.9296875) = .11101110
# ff_dec2bin(.06640625) = .000100010
# mantissa = .625
# mantissa = .06640625
# mantissa = .906339
# ff_dec2bin(.625) = .101
# ff_dec2bin(mantissa)

""" this program is a transformation from 'n' decimal number to binary number - only mantissa!"""

import math
import sys
from bitstring import Bits

#list comprehensions: 
sqrt_inv = [ 1/(2.**x) for x in range(1,55) ]

def insert (source_str, insert_str, pos):
    return source_str[:pos]+insert_str+source_str[pos:]
    
def ff_dec2bin(n):
    ig = math.floor(n)
    fl=n-ig
   
    sc = 1 if (n>0) else 0
    len = int(math.fabs(math.ceil(math.log2(math.fabs(n)))+1 ))
    
    b= Bits(int=int(ig), length=len)
    nstr=b.bin
    
    in_binary = ""
    for number in range(54):
        valor = sqrt_inv[number]       
        if fl - valor >= 0:
            in_binary += in_binary.join("1")
            fl = fl - valor        
        else:
            in_binary += in_binary.join("0")
        if fl == 0.0:
            break        
    return nstr[sc:]+"." + in_binary

def isfloat(value):
  try:
    float(value)
    return True
  except ValueError:
    return False


def findexp(nstr):
    expn=0;
    if nstr[0]=='1':
        expn=nstr.find(".")-1    #1001.000110
        allOnes = True
        for i in range(0, expn+1):

            if (nstr[i]=='0'):
                allOnes = False
                break;

        man = nstr.replace(".", "")
        man=insert(man, ".", 1)
        if (allOnes):    #1111.101 = 1.101
            nnstr = nstr
            nstr="1." + nnstr[expn+2:]
            man = "0." + nnstr[expn+2:]
            expn=0
    else:
        if (nstr.find(".")==1):   #0.0001
            expn=-nstr.find("1")+1
            if nstr[-expn+2:]=="":
                man = "0.0"
            else:
                man ="0."+nstr[-expn+2:]
        else:
            print("not sure")
        
    
    return [man, expn, nstr]

# return float number with exponent, mentissa and fixpoint expression
def getconv(n):
    nstr=ff_dec2bin(n)
    man, exp, nstr = findexp(nstr)
    
    return man, exp, nstr

if __name__ == "__main__":
    if len(sys.argv)==2:
        num=float(sys.argv[1])
        man, expr, nstr=getconv(num)

        print(nstr, man, expr)
    else:
        print("%s num"% (sys.argv[0]))