num = 600851475

def isPrime(x):
    for count in range(2, x):
        if x % count ==0:
            return False
    return True

for x in range(num, 0, -1):
    if num % x ==0:
        if isPrime(x) == True:
            print(str(x) + " is the lagest prime factor")
            break

