# Method to generate small primes in a list.
def genPrimes():
    primes = []
    for i in range(2,1299827):
        prime=True
        for j in range(2,int(i/2+1)):
            if i%j==0:
                prime=False
                break
        if prime:
            primes.append(i)
    f = open("prime_list.txt", "w")
    for i in range(len(primes)-2):
        f.write(str(prime_item) + ", ")
    f.write(str(primes[-1]))