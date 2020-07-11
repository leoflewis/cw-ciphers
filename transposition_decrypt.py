cipher_text = "16 12 8 4 0 1 5 9 13 17 18 14 10 6 2 3 7 11 15 19"
cipher_list = list(cipher_text.split())

cols = 4 
rows = 5
key = '-1 2 -3 4'
translation_matrix = [None] * cols
plaintext = ''
start = 0
stop = rows

key_int = [int(i) for i in key.split()]

for k in key_int:
    if k < 0:
        col_items = cipher_list[start:stop]
    elif k > 0:
        col_items = list((reversed(cipher_list[start:stop])))
    translation_matrix[abs(k) - 1] = col_items
    start += rows
    stop += rows

print("\nciphertext = {}".format(cipher_text))
print("\ntranslation matrix = {}", *translation_matrix, sep="\n")
print("\nkey length = {}".format(len(key_int)))

for i in range(rows):
    for col_items in translation_matrix:
        word = str(col_items.pop())
        plaintext += word + " "
    
print('\nplaintext = {}'.format(plaintext))