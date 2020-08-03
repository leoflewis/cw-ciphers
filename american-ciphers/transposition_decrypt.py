#Program to decrypt transposition route cipher from the Unionin the american civil war

def decrypt(cipher_text, cols, rows):
    #Text to be decrypted
    cipher_list = list(cipher_text.split())

    #Key tells which direction to iterate over for every row
    key = "-1 2 -3 4"

    #Empty placeholder for ciphertext to written to in order
    translation_matrix = [None] * cols

    #Empty placeholder for final plaintext string
    plaintext = ''

    #Variables to point to location within columns
    start = 0
    stop = rows

    #Create list of numbers within key
    key_int = [int(i) for i in key.split()]

    #Loop over every element of the key
    for k in key_int:
        #Whether or not the elemnt of the key is positive or negative tells us whci direction the columns should be read in 
        #columns will be read front to back later
        if k < 0:
            #If ellement of key is less than zero its already in order, add it to temporary location
            col_items = cipher_list[start:stop]
        elif k > 0:
            #otherwise reverse it and store it temporary location
            col_items = list((reversed(cipher_list[start:stop])))
        #add all lists from temporary location to another list
        translation_matrix[abs(k) - 1] = col_items
        #update variables that point in columns by column length
        start += rows
        stop += rows

    #print cipher text, the list of columns that has just been placed in order and the amount of elements in the key
    print("\nciphertext = {}".format(cipher_text))
    print("\ntranslation matrix = ", *translation_matrix, sep="\n")
    print("\nkey length = {}".format(len(key_int)))

    #from each ordered column remove last element and add to plaintext holder
    for i in range(rows):
        for col_items in translation_matrix:
            word = str(col_items.pop())
            plaintext += word + " "
        
    #print plain text
    print('\nplaintext = {}'.format(plaintext))
    return str(plaintext)

def main():
    cipher_text = str(input("Enter cipher text:"))
    #Number of columns and rows in transposition cipher matrix
    cols = int(input("enter columns:"))
    rows = int(input("enter rows:"))
    decrypt(cipher_text, cols, rows)

if __name__ == "__main__":
    main()