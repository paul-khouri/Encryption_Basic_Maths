from decimal import *
getcontext().prec=100
print(getcontext())
print(Decimal(1)/Decimal(3))
x=(Decimal(1)//Decimal(3))
print(x)
