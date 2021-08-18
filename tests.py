
def power_mod(a,exp,n):
    binary = "{0:b}".format(exp)
    str_binary = str(binary)
    length = len(str_binary)
    power_list=[a]

    v = a
    for i in range(1,length):
        v = v*v%n
        power_list.append(v)

    c = length -1
    total_value = 1

    for x in str_binary:
        if x == "1":
            total_value = (total_value*power_list[c])%n
        c-=1
    return total_value


import math


# satisfies ax+by = d where d= gcb(a,b)
# a must be greater than b
def extended_EA(a, b):
    # test a>b
    if a <= b:
        print("a is less than b")
        return None
    if b == 0:
        d = a
        x = 1
        y = 0
        return d, x, y
    x_2 = 1
    x_1 = 0
    y_2 = 0
    y_1 = 1
    while b > 0:
        q = math.floor(a / b)
        r = a - q * b
        x = x_2 - q * x_1
        y = y_2 - q * y_1
        a = b
        b = r
        x_2 = x_1
        x_1 = x
        y_2 = y_1
        y_1 = y
    d = a
    x = x_2
    y = y_2
    # y is the inverse
    return d, x, y

def get_inverse(a,n):
    d,x,y = extended_EA(n,a)
    if y<0:
        y += n
    test = ( a*y )%n
    print( "{} * {} = {} mod {}".format(a,y,test, n))
    return y



def test(a, x, b, y, d):
    output = "{}*{} + {}*{} = {}".format("a", "x", "b", "y", "d")
    print(output)
    output = "{}*{} + {}*{} = {}".format(a, x, b, y, d)
    print(output)
    output = "{}*{} + {}*{} = {}".format("e", "x", "n", "y", "1")
    print(output)
    output = "{}*{} + {}*{} = {}".format(b, y, a, x, d)
    print(output)
    if a * x + b * y != d:
        print("Abusive message")
    else:
        print("Yeah {}*{} + {}*{} = {}".format(a, x, b, y, d))
        print("{}+{}={}".format(y, a, y + a))






if __name__ == "__main__":
    a = 1250104
    b = 3


    #d, x, y = extended_EA(a, b)
    #test(a, x, b, y, d)
    # if e(=b) is coprime to n(=a) then y is the multiplicative inverse
    # of b
    #d, x, y = extended_EA(a, b)
    n = 10
    a = 7
    get_inverse(a,n)
    #power_mod(2,6,7)
