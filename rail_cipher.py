#Rail cipher from the civil war
#Impractical python projects chapter 4

#main method to receive plain text and pass to encryption method
def main():
    plain_text = str(input("Enter plaintext:"))
    encrypt(plain_text)

#Encryption method
def encrypt(plaintext):
    #convert to upper case, split and then rejoin with each char as one element in one list
    plain_list = list("".join(plaintext.upper().split()))
    #divide into two lists, one with odd indexes from original list and one with even indexes
    list_one = plain_list[::2]
    list_two = plain_list[1::2]
    #place elements back into original list
    #every other char from original list, folllowed by every other char from second half of orginal list
    cipher_text = list_one + list_two
    #convert to string
    rails = ''.join(cipher_text)
    #place space every 5 characters 
    cipher_text = ' '.join(rails[i:i+5] for i in range(0, len(rails), 5))
    return cipher_text
    
 
if __name__ == "__main__":
    main()