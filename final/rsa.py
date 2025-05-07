from math import gcd

# Function to compute modular inverse
def modinv(a, m):
    for x in range(1, m):
        if (a * x) % m == 1:
            return x
    return None

# RSA Implementation
def rsa():
    # Input primes and message
    p = int(input("Enter first prime number (p): "))
    q = int(input("Enter second prime number (q): "))
    msg = int(input("Enter message to encrypt (integer): "))

    n = p * q
    z = (p - 1) * (q - 1)

    print(f"Value of N = (P * Q) => = {n}")
    print(f"The value of z (φ(n)) = (P-1)*(Q-1) = {z}")

    # Choose e such that 1 < e < z and gcd(e, z) == 1
    e = 2
    while e < z:
        if gcd(e, z) == 1:
            break
        e += 1

    print(f"The value of e (public key exponent) = {e}")

    # Compute d (modular inverse of e mod z)
    d = modinv(e, z)
    print(f"The value of d (private key exponent) = {d}")

    print("*" * 55)
    print(f"\tYour Public key = {{ {e} , {n} }}")
    print(f"\tYour Private key = {{ {d} , {n} }}")
    print("*" * 55)

    # Encrypt message: c = msg^e mod n
    c = pow(msg, e, n)
    print(f"Encrypted message (ciphertext) = {c}")

    # Decrypt message: m = c^d mod n
    decrypted = pow(c, d, n)
    print(f"Decrypted message = {decrypted}")

# Run the RSA function
rsa()
