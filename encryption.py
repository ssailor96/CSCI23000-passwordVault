#file for encryption and decryption of vault

# import pycrypto

#for this i've decided to use AES 256 encryption with CBC (cipher block chain)
# 


def encryption(self):
    # Info obtained from : http://stackoverflow.com/questions/12524994/encrypt-decrypt-using-pycrypto-aes-256
    '''
    Steps
    1. load content
    2. pad content to make it proper block length (I planned on using PKCS7)
       Link to info on padding : https://en.wikipedia.org/wiki/Padding_(cryptography)#PKCS7
    3. Create an IV (Initializaion Vector)
       Link to info on IV: https://en.wikipedia.org/wiki/Initialization_vector
    4. Create an instance of AES and set the mode CBC
       Link to info on CBC : https://en.wikipedia.org/wiki/Block_cipher_mode_of_operation
    5. Concatinate the IV with the Encrypted Content
    6.  BaseEncode64 the encrypted content
       Link to info on BaseEncode : https://en.wikipedia.org/wiki/Base64
    7. Return encrypted content

    '''

    return

def decryption(self):
    
    '''
    Steps
    1. BaseDecode64 encrypted content
    2. Using the key and the iv, decrypt content
    3. Unpad content 
    4. Return decoded

    '''

    return

