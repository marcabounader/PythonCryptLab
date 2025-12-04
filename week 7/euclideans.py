import sys
def extended_gcd(a, b):
    """
    Implements the Extended Euclidean Algorithm to find gcd(a, b) and
    coefficients x and y such that ax + by = gcd(a, b).
    """
    if a == 0:
        return b, 0, 1
    else:
        gcd, x1, y1 = extended_gcd(b % a, a)
        x = y1 - (b // a) * x1
        y = x1
        return gcd, x, y

def modular_multiplicative_inverse(a, m):
    """
    Calculates the modular multiplicative inverse of 'a' modulo 'm'
    using the Extended Euclidean Algorithm.
    Returns the inverse if it exists, otherwise raises an exception.
    """
    gcd, x, y = extended_gcd(a, m)

    if gcd != 1:
        raise Exception("Modular inverse does not exist (a and m are not coprime)")
    else:
        # Ensure the inverse is positive
        return x % m
    
