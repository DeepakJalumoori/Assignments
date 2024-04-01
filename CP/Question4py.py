'''Given three numbers a, b and m. Calculate (ab % m)
Example input :
2 5 3
Example output :
2
Explanation :
25 % 3 = 32 % 3 = 2'''


def power_modulo(base, exponent, modulus):
    result = 1

    base = base % modulus
    
    while exponent > 0:
        # If exponent is odd, multiply result with base and take modulo modulus
        if exponent % 2 == 1:
            result = (result * base) % modulus
        
        # Square base and take modulo modulus
        base = (base * base) % modulus

        # Divide exponent by 2
        exponent //= 2

    return result

if __name__ == "__main__":

    base = int(input("Enter the value of base (a): "))
    exponent = int(input("Enter the value of exponent (b): "))
    modulus = int(input("Enter the value of modulus (m): "))

    # (base^exponent % modulus)
    result = power_modulo(base, exponent, modulus)

    print(f"The result of ({base}^{exponent} % {modulus}) is: {result}")
