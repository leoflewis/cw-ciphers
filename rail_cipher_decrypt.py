#program to decrypt ciphers using the rail cipher
#impractical python projects chapter 4

import math
import itertools

#main method to pass chipher text to decryption method
def main():
    cipher_text = input("Enter cipher text:")
    decrypt(cipher_text)

#decryption method
def decrypt(ciphertext):
    #remove whitepsace
    message = "".join(ciphertext.split())
    #split message in half
    row1_len = math.ceil(len(message) / 2)
    row1 = (message[:row1_len])
    row2 = (message[row1_len:])
    plaintext = []
    #merge lists
    for row1, row2 in itertools.zip_longest(row1, row2):
        plaintext.append(row1.lower())
        plaintext.append(row2.lower())
    if None in plaintext:
        plaintext.pop()
    #merge chars
    print("plaintext: {}".format(''.join(plaintext)))
    return ''.join(plaintext)

if __name__ == "__main__":
    main()