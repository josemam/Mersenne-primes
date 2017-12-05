# Auxiliary functions

# Gives the corresponding Mersenne prime with the given exponent.

def mersennePrime(exponent):
    return int(pow(2,exponent)-1)

# Test wether the Mersenne prime candidate is prime with Lucas-Lehmer primality test.
# Lucas Lehmer only works with even exponents.

def isPrimeLL(exponent):
    if exponent%2==0:
        return exponent==2

    s=4
    number = mersennePrime(exponent)
    while exponent>2:
        s=int((s*s - mersennePrime(2))%number)
        exponent-=1

    return s==0;