##n = pq, where p and q are distinct primes.
##ϕ = (p−1)(q−1)
##e<n such that gcd(e,ϕ)=1
##d=e^−1mod ϕ
##c=m^e mod n,1<m<n
##m=c^d mod n


import math
from decimal import *
getcontext().prec=100

# p, q MUST be prime
# uncomment a p, q
# and comment out the other
#p= 23
#q = 31
#q = 1229
#p = 99119
#q = 99131
#p = 57322081
#q = 42657851
#p=7216922249
#q=1917844787
#p = 11443576439306602211
#q = 71576491244400381023
p = 98391773137114388472898079588209381708336043358203
q = 70401528712933778755874484909703053789592374934061

n = p * q
totient = (p - 1) * (q - 1)


def find_coprime(tot):
    i = 4
    while math.gcd(tot, i) != 1:
        i += 1
    # print("done")
    return i




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
        q = Decimal(a)//Decimal(b)
        #print("{} = {}/{}".format(q,a,b))
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
    y= int(y)
    if y<0:
        y += n
    test = ( a*y )%n
    #print( "{} * {} = {} mod {}".format(a,y,test, n))
    return y





def compute_mod(a,exp,n):
    print("c = {} ^ {} mod {}".format(a, exp, n))
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

print("Two large primes p, q are generated")
print("p = {} , q = {}".format(p, q))
print("In an actual case these would be at least 300 digits long")
print("Calculate n = pq")
print("n= {}".format(n))
print("This creates a substantially larger number, with only two factors p,q. ")
print("Finding these factors (for very large p, q) is, for all practical purposes, 'impossible'  ")
print()

e = find_coprime(totient)

d = get_inverse(e, totient)

print("Also compute: totient = (p-1)(q-1) = {}".format(totient))
print("And compute:  e such that 1< e <totient and gcd(e, totient = 1), e = {}".format(e))
print("And compute:  d such that 1< d <totient and ed = 1 mod (totient),d = {}".format(d))
print("Public Key is (n,e), ({},{})".format(n, e))
print("Private Key is (p,q,d), ({},{},{})".format(p, q, d))
print()
#457505867
# write your message here
# message must be less that the mondulus (n)
# has a safety below to use half the mod.
message = 8346836836835684
if message > n:
    message = math.floor(n / 2)

print("Message to send: {}".format(message))
code = compute_mod(message, e, n)  # math.pow(message,e)%n
print("Encrypted message sent to receiver: {}".format(code))
decrypt = compute_mod(code, d, n)
print("Message decrypted by receiver: {}".format(decrypt))


