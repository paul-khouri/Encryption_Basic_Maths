import math
def createGroup(n):
    temp = []
    for x in range(0,n+1):
        # start row
        row = []
        for y in range(0,n+1):
            if x == 0 and y ==0:
                row.append(" ")
            elif x == 0:
                row.append(y-1)
            elif y == 0:
                row.append(x-1)
            else:
                row.append( (row[0]*temp[0][y])%n )
        temp.append(row)
    #print(temp)
    return temp

def printGroup(g):
    for x in g:
        temp =""
        for y in x:
            temp += "{:3}".format(y)
        print(temp)

# number index modulus
def mod_power(a,j,n):
    output_set = set()
    v = a
    if a >= n:
        a= a%n
        print("a has been modded")
    #output = "{} power 1 mod {} = {}".format(a,n,a)
    output_set.add(v)
    #print(output)
    for i in range(1,j):
        v = (v*a)%n
        output_set.add(v)
        if(i == j-1):
            output = "{} power {} mod {} = {}".format(a,i+1, n, v)
            print(output)
        #temp = "{:<100f}".format(math.pow(a,i+1)%n)
        #print(temp)
    if len(output_set) == totient(n):
        output = "{} is a primitive root of {}".format(a,n)
        print(output)
    return v

def mod_power_print_set(a,n):
    v = a
    output_set = set()
    if a >= n:
        a= a%n
        print("a has been modded")
    output_set.add(v)
    output = "{} power 1 mod {} = {}".format(a,n,a)
    print(output)
    for i in range(1,n):
        v = (v*a)%n
        output_set.add(v)
        output = "{} power {} mod {} = {}".format(a, i + 1, n, v)
        print(output)
    if len(output_set) == totient(n):
        output = "{} is a primitive root of {}".format(a,n)
        print(output)


def prime_primitive_root(a,n):
    return None

def get_coprime_set(n):
    co_set = []
    for i in range(1,n):
        if math.gcd(i,n)== 1:
            co_set.append(i)
    #print(co_set)
    return co_set

def totient(n):
    return len(get_coprime_set(n))

def seconds_in_n_years(n):
    s = 60*60*24*365*n*1000
    t = str(s)
    print(   "{:50.0f} milliseconds in {} years ( {} digit number )".format(int(s),n,len(t) )  )

def get_full_power_list():
    n= 7481
    for x in get_coprime_set(n):
        if x!= 1:
            mod_power(x, n-1, n)

def alice_bob(a=3, b=4, g=5, p=23):
    A = mod_power(g,a, p)
    B = mod_power(g,b, p)
    A_s = mod_power(B,a, p)
    B_s = mod_power(A,b,p)


def big_power(a,p):
    n = math.pow(a,p)
    print(  "{:50.0f}".format(n) )


if __name__ == "__main__":
    #g=createGroup(10)
    #printGroup(g)
    #mod_power(2,6, 7)
    #get_coprime_set(15)
    #print(totient(7))
    #seconds_in_n_years(1000000000)
    #get_full_power_list()
    #alice_bob()
    #alice_bob(99,273,1274,7481)
    #alice_bob(11, 7, 5, 23)
    #alice_bob(2, 4, 7, 11)
    #big_power(10,25)
    #mod_power(5,4,99)
    mod_power_print_set(5,23)





