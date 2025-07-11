# RSA Cryptosystem Implementation

## Overview
This project implements a basic RSA cryptosystem in Python. RSA (Rivest-Shamir-Adleman) is an asymmetric encryption algorithm that uses a public key for encryption and a private key for decryption. This implementation demonstrates key generation, encryption, and decryption for educational purposes.

## Features
- Generates RSA public and private key pairs using random prime numbers.
- Encrypts and decrypts text messages using the RSA algorithm.
- Includes helper functions for prime number generation and modular arithmetic.
- Demonstrates the full encryption-decryption cycle with a sample message.

## Requirements
- Python 3.x
- Standard libraries: `random`, `math`

No external dependencies are required.

## Installation
1. Clone or download this repository.
2. Ensure Python 3 is installed on your system.
3. Run the `rsa_cryptosystem.py` script.

## Usage
1. Run the script:
   ```bash
   python rsa_cryptosystem.py
   ```
2. The script will:
   - Generate a public and private key pair.
   - Encrypt a sample message ("Hello, RSA!").
   - Decrypt the ciphertext and display the result.
3. Example output:
   ```
   Public key: (65537, 123457)
   Private key: (12345, 123457)
   Original message: Hello, RSA!
   Encrypted message: [12345, 67890, 54321, ...]
   Decrypted message: Hello, RSA!
   ```
4. To use the code with a custom message:
   - Modify the `message` variable in the `if __name__ == "__main__":` block.
   - Run the script again to see the encryption and decryption results.

## Code Structure
- `is_prime(n)`: Checks if a number is prime.
- `generate_prime(min_value, max_value)`: Generates a random prime number within a specified range.
- `mod_inverse(e, phi)`: Computes the modular multiplicative inverse using the extended Euclidean algorithm.
- `generate_keypair()`: Generates RSA public and private keys.
- `encrypt(public_key, plaintext)`: Encrypts a plaintext message using the public key.
- `decrypt(private_key, ciphertext)`: Decrypts a ciphertext using the private key.

## How RSA Works
1. **Key Generation**:
   - Select two prime numbers, \( p \) and \( q \).
   - Compute \( n = p \times q \) and \( \phi(n) = (p-1) \times (q-1) \).
   - Choose a public exponent \( e \) (typically 65537) coprime with \( \phi(n) \).
   - Compute the private exponent \( d \) such that \( d \times e \equiv 1 \pmod{\phi(n)} \).
2. **Encryption**: Convert the message to a number \( m \), then compute \( c = m^e \pmod{n} \).
3. **Decryption**: Compute \( m = c^d \pmod{n} \) to recover the original message.

## Limitations
- **Small Primes**: This implementation uses small prime numbers (100 to 1000) for simplicity. Real-world RSA uses much larger primes (e.g., 2048-bit) for security.
- **No Padding**: The code does not implement padding schemes like OAEP, making it unsuitable for production use.
- **Character-by-Character Encryption**: The implementation encrypts each character individually, which is inefficient and insecure for real applications.

## Security Notes
- Use large prime numbers (e.g., 2048-bit or higher) in production systems.
- Implement padding schemes (e.g., OAEP) to prevent attacks.
- Ensure proper key management and secure random number generation in real applications.

## Credits
- Implemented from scratch based on the RSA algorithm as described by Rivest, Shamir, and Adleman.
- No external code was directly adapted.

## License
This project is licensed under the MIT License. 