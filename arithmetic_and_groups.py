import math
import time


def print_line(d="-", length=30):
    print(d*length)


# default length 2
def get_int_tuple(m="Please enter a,n :-> ", length=2):
    cont = True
    while cont is True:
        v = input(m)
        tup = v.split(",")
        try:
            map_object = map(int, tup)
            _tup = tuple(map_object)
        except ValueError:
            print("Not valid integers")
            continue
        if len(_tup) != length:
            print("Do not have {} integers".format(length))
        else:
            return _tup


def get_integer(m, _min, _max):
    """ message, minimum and maximum returns acceptable integer """
    cont = True
    while cont is True:
        try:
            my_integer = int(input(m))
        except ValueError:
            print("please enter an integer value")
            continue
        if my_integer < _min:
            print("The value you have entered is too low")
            continue
        elif my_integer > _max:
            print("The value you have entered is too high")
            continue
        return my_integer


def get_single_entry(m):
    cont = True
    while cont is True:
        response_string = input(m).strip().upper()
        if len(response_string) != 1:
            print("Please enter only one character")
        else:
            return response_string


def confirmation(m="Please confirm: Y/N: -> "):
    c = ["Y","N"]
    while True:
        choice = input(m).upper()
        if choice not in c:
            print("Please choose from these options: {}".format(c))
        elif choice == "Y":
            return True
        else:
            return False


def create_arithmetic_group(n,op="*"):
    temp = []
    for x in range(0,n+1):
        # start row
        row = []
        for y in range(0,n+1):
            if x == 0 and y ==0:
                row.append(op)
            elif x == 0:
                row.append(y-1)
            elif y == 0:
                row.append(x-1)
            else:
                if op=="+":
                    row.append( (row[0]+temp[0][y])%n )
                else:
                    row.append((row[0] * temp[0][y]) % n)

        temp.append(row)
    return temp


def printGroup(g):
    for x in g:
        temp =""
        for y in x:
            temp += "{:>3}".format(y)
        print(temp)

# (a,n) tuple
def get_mod(t):
    return t[0]%t[1]


# number index modulus
def get_mod_power(a,j,n):
    v = a
    for i in range(1,j):
        v = (v*a)%n
    return v


def get_list_powers(a,n, to_print=True, primitive_root = False):
    output_set = set()
    for i in range(1,n):
        p=get_mod_power(a,i,n)
        output_set.add(p)
        if to_print:
            output = "{} power {} mod {} = {}".format(a, i,n , p)
            print(output)
    if primitive_root:
        if len(output_set) == totient(n):
            output = "{} is a primitive root of {}".format(a, n)
            #print(output)
            return True
        else:
            return False
    else:
        return None


def get_list_primitive_roots(n):
    t_s = time.time()
    root_set = []
    for i in range(2,n):
        result = get_list_powers(i,n,False, True)
        if result:
            root_set.append(i)
    t_f = time.time()
    total = t_f - t_s
    print(total)
    print(root_set)
    return root_set

# pirnt up to power in a list
def mod_power_print_set(a,j,n):
    v = a
    output = "{:3} power {:3} mod {:3} = {:3}".format(a, 1,n, a)
    print(output)
    for i in range(1,j):
        v = (v*a)%n
        output = "{:3} power {:3} mod {:3} = {:3}".format(a, i+1,n, v)
        print(output)
    return v

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



def alice_bob(a=4, b=3, g=5, p=23):
    output = "Public key is g = {} , p ={}".format(g,p)
    print(output)
    print_line(".", 20)
    A = get_mod_power(g,a, p)
    output = "Alice has secret key {}".format(a)
    print(output)
    output = "Alice computes {} pwr {} mod {} = {}".format(g,a,p,A)
    print(output)
    print("She publicly sends this to Bob")
    print_line(".",20)
    B = get_mod_power(g,b, p)
    output = "Bob has secret key {}".format(b)
    print(output)
    output = "Bob computes {} pwr {} mod {} = {}".format(g,b,p,B)
    print(output)
    print("He publicly sends this to Alice")
    print_line(".", 20)
    A_s = get_mod_power(B,a, p)
    output = "Alice computes {} pwr {} mod {} = {}".format(B,a,p, A_s)
    print(output)
    B_s = get_mod_power(A,b,p)
    output = "Bob computes {} pwr {} mod {} = {}".format(A,b,p, B_s)
    print(output)

def alice_bob_options():
    option_list = [
        {"a":351, "b":901, "g":483, "p":1009 },
        {"a": 8, "b": 13, "g": 5, "p": 23},
        {"a": 801, "b": 57, "g": 285, "p": 997},
        {"a": 1006, "b": 589, "g": 1526, "p": 1951},
    ]
    c = 0
    for x in option_list:
        print("{} : {}".format(c,x))
        c += 1
    choice = option_list[get_integer("Please choose option number: -> ", 0, c)]
    print_line("-", 20)
    alice_bob(choice["a"],choice["b"],choice["g"],choice["p"])








def main():
    menu ={
        "A":"Get Z_n+ ",
        "B":"Get Z_n* ",
        "C":"Get modulus of number (a,n)",
        "D":"Get modulus power of number (a,pwr,n)",
        "E":"For (a,n), get set of modulus powers up to n-1 ",
        "F":"For (a,n), check if a is a primitive root ",
        "G":"For n , get list of primitive roots ",
        "H": "For (a,pwr,n), print list up to pwr ",
        "I": "Alice and Bob - Diffie-Hellman ",
        "J": "Alice and Bob - Diffie-Hellman - Options ",
        "Q":"Quit  :-> "
    }
    while True:
        for x,y in menu.items():
            print("{}: {}".format(x,y))
        print_line()
        choice = get_single_entry("Please choose option: -> ")
        print_line()
        if choice == "A":
            n = get_integer("Please enter n: -> ",0,20)
            g = create_arithmetic_group(n, "+")
            printGroup(g)
        elif choice == "B":
            n = get_integer("Please enter n: -> ", 0, 20)
            g = create_arithmetic_group(n,"*")
            printGroup(g)
        elif choice == "C":
            t = get_int_tuple()
            m = get_mod(t)
            output= "{} mod {} = {}".format(t[0], t[1], m)
            print(output)
        elif choice == "D":
            t = get_int_tuple("Please enter a,p,n :-> ", 3)
            p = get_mod_power(t[0],t[1], t[2])
            output = "{} power {} mod {} = {}".format(t[0], t[1],t[2], p)
            print(output)
        elif choice == "E":
            t = get_int_tuple()
            get_list_powers(t[0],t[1])
        elif choice == "F":
            t = get_int_tuple()
            get_list_powers(t[0], t[1], True, True)
        elif choice == "G":
            n = get_integer("Please enter n: -> ", 0, 2000)
            get_list_primitive_roots(n)
        elif choice == "H":
            t = get_int_tuple("Please enter a,p,n :-> ", 3)
            mod_power_print_set(t[0],t[1], t[2])
        elif choice == "I":
            alice_bob()
        elif choice == "J":
            alice_bob_options()
        elif choice =="Q":
            if confirmation():
                break
        else:
            print("Unrecognised option")
        print_line()




if __name__ == "__main__":
    main()






