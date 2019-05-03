#KEEP ALL OF THIS
import pickle

enc={"a": 'y',
     "b": 'z',
    "c": 'a',
     'd': 'b',
     'e':'c',
     'f':'d',
     'g':'e',
     'h':'f',
     'i':'g',
     'j':'h',
     'k':'i',
     'l':'j',
    'm':'k',
    'n':'l',
     'o':'m',
     'p':'n',
     'q':'o',
     'r':'p',
     's':'q',
     't':'r',
     'u':'s',
     'v':'t',
     'w':'u',
     'x':'v',
     'y':'w',
     'z':'x'}

dec={'a':'c',
     'b':'d',
     "c":'e',
     'd':'f',
     'e':'g',
     'f':'h',
     'g':'i',
     'h':'j',
     'i':'k',
     'j':'l',
     'k':'m',
     'l':'n',
     'm':'o',
     'n':'p',
     'o':'q',
     'p':'r',
     'q':'s',
     'r':'t',
     's':'u',
     't':'v',
     'u':'w',
     'v':'x',
     'w':'y',
     'x':'z',
     'y': 'a',
     'z': 'b'
     }

def encrypt(text):
    texts=[text]
    for i, word in enumerate(texts):
        for key in enc:
            print(key)
            print(texts)
            texts[i] = texts[i].replace(key, enc.get(key))
    return texts

def decrypt2(text):
    texts=[text]
    for i, word in enumerate(texts):
        for key in dec:
            print(key)
            print(texts)
            texts[i] = texts[i].replace(key, dec.get(key))
    return texts

"""
prompt=input("Text to encrypt: ")
encrypted_prompt=encrypt(prompt)
print(encrypted_prompt)

prompt=input("Text to decrypt: ")
decrypted_prompt=decrypt2(prompt)
print(decrypted_prompt)
"""

# WORKING VERSION USE FOR SIA
import string

CHAR_SET=string.printable[:-5]
SUBSTITUTION_CHAR = CHAR_SET[-3:]+CHAR_SET[:-3]

ENCRYPTION_DICT={}
DECRYPTION_DICT={}
for i,k in enumerate(CHAR_SET):
    v = SUBSTITUTION_CHAR[i]
    ENCRYPTION_DICT[k]=v
    DECRYPTION_DICT[v]=k

for c in string.printable[-5:]:
    ENCRYPTION_DICT[c]=c
    DECRYPTION_DICT[c]=c

INPUT_FILE_NAME="cryptopy_input.txt"
OUTPUT_FILE_NAME="cryptopy_output.txt"
def encrypt_msg(plaintext,encrypt_dict):
    ciphertext=[]
    for k in plaintext:
        v = encrypt_dict[k]
        ciphertext.append(v)
    return  ''.join(ciphertext)

def decrypt_msg(ciphertext, decrypt_dict):
    plaintext=[]
    for k in ciphertext:
        v = decrypt_dict[k]
        plaintext.append(v)
    return ''.join(plaintext)

if __name__=="__main__":
    ENCRYPT=True
    with open(INPUT_FILE_NAME, 'r') as input_file:
        message=input_file.read()

    if ENCRYPT:
        text_to_output = encrypt_msg(message, ENCRYPTION_DICT)
    else:
        text_to_output=decrypt_msg(message, DECRYPTION_DICT)

    print(text_to_output)

    with open(OUTPUT_FILE_NAME, 'w') as output_file:
        output_file.write(text_to_output)
