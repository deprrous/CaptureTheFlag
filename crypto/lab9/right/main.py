from modes import *

if __name__ == "__main__":
    # Read plaintext from file
    with open(r"/home/dep/crypto/lab9/right/data.txt", "r") as f:
        plaintext = f.read()
    
    # Define encryption parameters
    shift = 3           # Caesar Cipher shift
    a, b = 5, 8         # Affine Cipher keys
    iv = 'J'            # Initialization vector for CBC and OFB
    nonce = ord('A')    # Nonce for CTR

    # Testing CBC Mode with Caesar Cipher
    print("\nTesting CBC Mode with Caesar Cipher")
    cbc_caesar_ciphertext = encrypt(plaintext, 'CBC', 'Caesar', shift, iv)
    cbc_caesar_decrypted_text = decrypt(cbc_caesar_ciphertext, 'CBC', 'Caesar', shift, iv)
    print("CBC Caesar Encrypted:", cbc_caesar_ciphertext)
    print("CBC Caesar Decrypted:", cbc_caesar_decrypted_text)

    # Testing OFB Mode with Affine Cipher
    print("\nTesting OFB Mode with Affine Cipher")
    ofb_affine_ciphertext = encrypt(plaintext, 'OFB', 'Affine', (a, b), iv)
    ofb_affine_decrypted_text = decrypt(ofb_affine_ciphertext, 'OFB', 'Affine', (a, b), iv)
    print("OFB Affine Encrypted:", ofb_affine_ciphertext)
    print("OFB Affine Decrypted:", ofb_affine_decrypted_text)

    # Testing CTR Mode with Caesar Cipher
    print("\nTesting CTR Mode with Caesar Cipher")
    ctr_caesar_ciphertext = encrypt(plaintext, 'CTR', 'Caesar', shift, nonce)
    ctr_caesar_decrypted_text = decrypt(ctr_caesar_ciphertext, 'CTR', 'Caesar', shift, nonce)
    print("CTR Caesar Encrypted:", ctr_caesar_ciphertext)
    print("CTR Caesar Decrypted:", ctr_caesar_decrypted_text)

    # Testing CBC Mode with Affine Cipher
    print("\nTesting CBC Mode with Affine Cipher")
    cbc_affine_ciphertext = encrypt(plaintext, 'CBC', 'Affine', (a, b), iv)
    cbc_affine_decrypted_text = decrypt(cbc_affine_ciphertext, 'CBC', 'Affine', (a, b), iv)
    print("CBC Affine Encrypted:", cbc_affine_ciphertext)
    print("CBC Affine Decrypted:", cbc_affine_decrypted_text)

    # Testing OFB Mode with Caesar Cipher
    print("\nTesting OFB Mode with Caesar Cipher")
    ofb_caesar_ciphertext = encrypt(plaintext, 'OFB', 'Caesar', shift, iv)
    ofb_caesar_decrypted_text = decrypt(ofb_caesar_ciphertext, 'OFB', 'Caesar', shift, iv)
    print("OFB Caesar Encrypted:", ofb_caesar_ciphertext)
   
