"""

Code an implementation that asks the user to input plaintext and an integer key, and encrypts the given text
 as follows. The alphabet used is 'ABCDEFGHIJKLMNOPQRSTUVWXYZÅÄÖ0123456789 '. Each letter of the plaintext is
replaced by the character found by moving forward in the alphabet by the number of characters equal to the key.
The alphabet is treated as circular, meaning that after the last character, it wraps around to the first character,
and similarly, the character before the first character is the last character.

"""


ALPHABET = "ABCDEFGHIJKLMNOPQRSTUVWXYZÅÄÖ0123456789 "

def encrypt(plaintext: str, key: int) -> str:
    result = []
    n = len(ALPHABET)


    for char in plaintext:
        if char in ALPHABET:
            index = ALPHABET.index(char)
            new_index = (index + key) % n
            result.append(ALPHABET[new_index])
        else:
            # если встретится символ не из алфавита / symbols not from the list
            result.append(char)

    return "".join(result)


plaintext = input("Input plaintext: ")
key = int(input("Input an integer for encoding: "))

ciphertext = encrypt(plaintext, key)
print(ciphertext)