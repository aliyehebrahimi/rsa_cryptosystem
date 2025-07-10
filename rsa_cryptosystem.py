import random
import math

def is_prime(n):
    """Check if a number is prime."""
    if n < 2:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

def generate_prime(min_value, max_value):
    """Generate a random prime number within a range."""
    prime = random.randint(min_value, max_value)
    while not is_prime(prime):
        prime = random.randint(min_value, max_value)
    return prime

def mod_inverse(e, phi):
    """Compute the modular multiplicative inverse of e mod phi."""
    def egcd(a, b):
        if a == 0:
            return b, 0, 1
        gcd, x1, y1 = egcd(b % a, a)
        x = y1 - (b // a) * x1
        y = x1
        return gcd, x, y
    
    gcd, x, _ = egcd(e, phi)
    if gcd != 1:
        raise ValueError("mod_inverse does not exist")
    return x % phi

def generate_keypair():
    """Generate RSA public and private keypair."""
    # Generate two prime numbers
    p = generate_prime(100, 1000)
    q = generate_prime(100, 1000)
    while p == q:
        q = generate_prime(100, 1000)
    
    # Compute n and phi
    n = p * q
    phi = (p - 1) * (q - 1)
    
    # Choose e (public exponent)
    e = 65537
    while math.gcd(e, phi) != 1:
        e = random.randint(3, phi - 1)
    
    # Compute d (private exponent)
    d = mod_inverse(e, phi)
    
    return (e, n), (d, n)

def encrypt(public_key, plaintext):
    """Encrypt the plaintext using the public key."""
    e, n = public_key
    # Convert each character to a number and encrypt
    cipher = [pow(ord(char), e, n) for char in plaintext]
    return cipher

def decrypt(private_key, ciphertext):
    """Decrypt the ciphertext using the private key."""
    d, n = private_key
    # Decrypt each number and convert back to characters
    plain = [chr(pow(char, d, n)) for char in ciphertext]
    return ''.join(plain)

# Demonstration
if __name__ == "__main__":
    # Generate keys
    public_key, private_key = generate_keypair()
    print(f"Public key: {public_key}")
    print(f"Private key: {private_key}")
    
    # Test message
    message = "Hello, RSA!"
    print(f"Original message: {message}")
    
    # Encrypt
    encrypted_msg = encrypt(public_key, message)
    print(f"Encrypted message: {encrypted_msg}")
    
    # Decrypt
    decrypted_msg = decrypt(private_key, encrypted_msg)
    print(f"Decrypted message: {decrypted_msg}")