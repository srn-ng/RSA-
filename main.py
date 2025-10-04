from fonction import is_prime_miller_rabin, extended_gcd
import math
import random

def main():
    try:
        p = int(input("Enter a prime number p: "))
    except ValueError:
        print("Invalid input for p (must be an integer).")
        return

    if not is_prime_miller_rabin(p):
        print("p is not prime.")
        return

    try:
        q = int(input("Enter a prime number q: "))
    except ValueError:
        print("Invalid input for q (must be an integer).")
        return

    if not is_prime_miller_rabin(q):
        print("q is not prime.")
        return

    # Calcul de n et phi(n)
    n = p * q
    phi_n = (p - 1) * (q - 1)

    ###### choosing e : public key ######
    list_of_public_key = []
    for e in range(2, phi_n):
        if math.gcd(e, phi_n) == 1:
            list_of_public_key.append(e)

    e = random.choice(list_of_public_key)

    # Calcul de d (clé privée)
    gcd, x, y = extended_gcd(e, phi_n)
    if gcd == 1:
        d = x % phi_n  # pour que d soit positif
        print(f"\nPublic key (e, n): ({e}, {n})")
        print(f" Private key (d, n): ({d}, {n})")
    else:
        print("e and phi_n are not coprime, choose another e.")

    
    mode = input("Do you want to (E)ncrypt or (D)ecrypt a message? ").strip().lower()

    if mode == 'e':
        message = input("Enter a message to encrypt: ")
        message_numbers = [ord(ch) for ch in message]
        encrypted = [pow(m, e, n) for m in message_numbers]
        print("Encrypted message:", encrypted)
    
    elif mode == 'd':
        encrypted_input = input("Enter numbers to decrypt (comma-separated): ")
        encrypted_numbers = [int(x.strip(" []")) for x in encrypted_input.split(",")]
        decrypted_numbers = [pow(c, d, n) for c in encrypted_numbers]
        decrypted_message = ''.join(chr(num) for num in decrypted_numbers)
        print("Decrypted message:", decrypted_message)
    
    else:
        print("Invalid choice. Please enter 'E' or 'D'.")
    
    

if __name__ == "__main__":
    main()