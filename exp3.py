def encrypt_transposition_cipher(key, plaintext, subkey):
    encrypted_text = ""
    for char in plaintext:
        if(char == " "):
            encrypted_text += "#"
        else:
            ascii = ord(char)
            ascii = ascii + subkey
            encr_char = chr(ascii)
            encrypted_text += encr_char
    
    print(encrypted_text)
    num_rows = (len(encrypted_text) // key ) + 1
    num_col = key
    # Create the matrix
    matrix = [[' ' for _ in range(num_col)] for _ in range(num_rows)]
    
    # Fill the matrix with characters from the plaintext
    index = 0
    for row in range(num_rows):
        for col in range(num_col):
            if index < len(plaintext):
                matrix[row][col] = encrypted_text[index]
                index += 1
    print(matrix)

    # transpose
    num_rows_transpose = num_col
    num_cols_transpose = num_rows

    cipher_matrix = [[ ' ' for _ in range(num_cols_transpose)] for _ in range(num_rows_transpose)]
    ciphertext = ""
    for rows in range(num_rows_transpose):
        for cols in range(num_cols_transpose):
            cipher_matrix[rows][cols] = matrix[cols][rows]
            ciphertext += cipher_matrix[rows][cols]
    print(cipher_matrix)
    print(ciphertext)
    return ciphertext


key = int(input("Enter the transkey key : "))
subkey = int(input("Enter the substitution key : "))
plaintext = input("Enter the plain text : ")
ciphertext = encrypt_transposition_cipher(key, plaintext, subkey )
print("Ciphertext:", ciphertext)

