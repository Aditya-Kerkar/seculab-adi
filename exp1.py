#Monoalphabetic cipher

def encrypt(Plaintext, subkey):
    encrypted_text = ""
    for char in Plaintext:
        if(char == " "):
            encrypted_text += "#"
        else:
            ascii = ord(char)
            ascii = ascii + subkey
            encr_char = chr(ascii)
            encrypted_text += encr_char
    
    return encrypted_text

def decrypt(encryptedtext, subkey):
    decrypted_text = ""
    for char in encryptedtext:
        if(char == "#"):
            decrypted_text += " "
        else:
            ascii = ord(char)
            ascii = ascii - subkey
            encr_char = chr(ascii)
            decrypted_text += encr_char
    
    return decrypted_text

plaintext = input("Enter palin text : ")
subkey = int(input("Enter Substitution key : "))

encrypted = encrypt(plaintext,subkey)
print(encrypted)

plain = decrypt(encrypted,subkey)
print(plain)    
