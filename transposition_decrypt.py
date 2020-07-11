#Program to decrypt transposition route cipher from the Unionin the american civil war

#Text to be decrypted
cipher_text = "16 12 8 4 0 1 5 9 13 17 18 14 10 6 2 3 7 11 15 19"
cipher_list = list(cipher_text.split())

#Number of columns and rows in matrix
cols = 4
rows = 5

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

#remove ordered columns and then remove every element from each column and add to plaintext holder
for i in range(rows):
    for col_items in translation_matrix:
        word = str(col_items.pop())
        plaintext += word + " "
    
#print plain text
print('\nplaintext = {}'.format(plaintext))