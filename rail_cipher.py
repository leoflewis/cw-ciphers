#Rail cipher from the civil war
#Impractical python projects chapter 4

#
def main():
    plain_text = str(input("Enter plaintext:"))
    encrypt(plain_text)

def encrypt(plaintext):
    plain_list = list("".join(plaintext.upper().split()))
    list_one = plain_list[::2]
    list_two = plain_list[1::2]
    plain_list[::2] = list_one
    plain_list[1::2] = list_two
    cipher_text = list_one + list_two
    rails = ''.join(cipher_text)
    print(' '.join(rails[i:i+5] for i in range(0, len(rails), 5)))
    
 
if __name__ == "__main__":
    main()