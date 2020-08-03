import transposition_decrypt, rail_cipher, rail_cipher_decrypt

#single test for transposition cipher
def test_transposition():
    ciphertext = "16 12 8 4 0 1 5 9 13 17 18 14 10 6 2 3 7 11 15 19"
    plaintext = "0 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 "
    cols = 4
    rows = 5
    print("transposition cipher:")
    assert transposition_decrypt.decrypt(ciphertext,cols, rows) == plaintext

#single test for rail cipher
def test_rail():
    print("rail cipher:")
    plaintext = "Buy more Maine potatoes"
    ciphertext = "BYOEA NPTTE UMRMI EOAOS"
    print("plaintext:", plaintext)
    print("ciphertext:", ciphertext)
    p_wo_white = str(plaintext.replace(" ", "").lower())
    print("plaintext without whitespace:",p_wo_white)
    assert rail_cipher_decrypt.decrypt(ciphertext) == p_wo_white
    assert rail_cipher.encrypt(plaintext) == ciphertext

def main():
    test_transposition()
    test_rail()

if __name__ == "__main__":
    main()