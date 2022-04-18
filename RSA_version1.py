##n = pq, where p and q are distinct primes.
##ϕ = (p−1)(q−1)
##e<n such that gcd(e,ϕ)=1
##d=e^−1mod ϕ
##c=m^e mod n,1<m<n
##m=c^d mod n


import math

# p, q MUST be prime
p = 13
q = 17
n = p * q
totient = (p - 1) * (q - 1)


def find_coprime(tot):
    i = 2
    while math.gcd(tot, i) != 1:
        i += 1
    # print("done")
    return i


def find_d(e, tot):
    i = 2
    while (i * e) % tot != 1:
        i += 1
    return i


# message,e, n
def compute_mod(num, power, mod):
    print("c = {} ^ {} mod {}".format(num, power, mod))
    temp = num
    # loop generate result
    # as python can become inaccurate with large powers
    for i in range(1, power):
        temp = (temp % mod * num % mod) % mod
    return int(temp)


print("Two large primes p, q are generated")
print("p = {} , q={}".format(p, q))
print("In an actual case these would be at least 300 digits long")
print("Calculate n = pq")
print("n= {}".format(n))
print("This creates a substantially larger number, with only two factors p,q. ")
print("Finding these factors (for very large p, q) is, for all practical purposes, 'impossible'  ")
print()

e = find_coprime(totient)

d = find_d(e, totient)

print("Also compute: totient = (p-1)(q-1) = {}".format(totient))
print("And compute:  e such that 1< e <totient and gcd(e, totient = 1), e = {}".format(e))
print("And compute:  d such that 1< d <totient and ed = 1 mod (totient),d = {}".format(d))
print("Public Key is (n,e), ({},{})".format(n, e))
print("Private Key is (p,q,d), ({},{},{})".format(p, q, d))
print()

message = 6
if message > n:
    message = math.floor(n / 2)

print("Message to send: {}".format(message))
code = compute_mod(message, e, n)  # math.pow(message,e)%n
print("Encrypted message sent to receiver: {}".format(code))
decrypt = compute_mod(code, d, n)
print("Message decrypted by receiver: {}".format(decrypt))


