import transposition_decrypt

def test():
    ciphertext = "16 12 8 4 0 1 5 9 13 17 18 14 10 6 2 3 7 11 15 19"
    plaintext = "0 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 "
    cols = 4
    rows = 5
    assert transposition_decrypt.decrypt(ciphertext,cols, rows) == plaintext

test()