'''Given a number N, Print first N prime number starting from 2 and skipping every 
alternate prime number
Example Input:
5
Example Output:
2 5 11 17 23
Explanation :
▪ First few prime numbers are 2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31 …
▪ First five alternate prime numbers will be 2, 5, 11, 17, and 23'''



def is_prime(number):
    if number <= 1:
        return False
    if number <= 3:
        return True
    if number % 2 == 0 or number % 3 == 0:
        return False
    i = 5
    while i * i <= number:
        if number % i == 0 or number % (i + 2) == 0:
            return False
        i += 6
    return True

def print_alternate_primes(count):
    prime_count = 0
    num = 2
    while prime_count < count:
        if is_prime(num):
            print(num, end=" ")
            prime_count += 1
        num += 1
        while True:
            if is_prime(num):
                break
            num += 1
    print()

N = int(input("Enter the value of N: "))
print("Output:")
print_alternate_primes(N)
