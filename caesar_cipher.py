'''
The Caesar cipher is an ancient encryption algorithm used by Julius Caesar. It encrypts letters by shifting them over by a certain number of places in the alphabet. We call the length of shift the key. 

For example, if the key is 3, then A becomes D, B becomes E, C becomes F, and so on. To decrypt the message, you must shift the encrypted letters in the opposite direction. 

This program lets the user encrypt and decrypt messages according to this algorithm.
When you run the code, the output will look like this:

Do you want to (e)ncrypt or (d)ecrypt?
> e
Please enter the key (0 to 25) to use.
> 4
Enter the message to encrypt.
> Meet me by the rose bushes tonight.
QIIX QI FC XLI VSWI FYWLIW XSRMKLX.

Do you want to (e)ncrypt or (d)ecrypt?
> d
Please enter the key (0 to 26) to use.
> 4
Enter the message to decrypt.
> QIIX QI FC XLI VSWI FYWLIW XSRMKLX.
MEET ME BY THE ROSE BUSHES TONIGHT.
'''

import string

alphabet_dict = {}

for index, letter in enumerate(string.ascii_uppercase):
    alphabet_dict[letter] = index
    alphabet_dict[index] = letter

def cypher(key_n, msg, encript= True):
    #encript = True
    msg = msg.upper()
    return_msg = ''
    
    for char in msg:
        if char in alphabet_dict:
            num = alphabet_dict[char]
            
            if encript:
                key = (num + key_n) % 26
                return_msg += alphabet_dict[key] #encryption
                
            else:
                key = (num - key_n) % 26
                return_msg += alphabet_dict[key] #decryption
                
        elif char == ' ':
            return_msg += ' '
        elif char == '.':
            return_msg += '.'
        elif type(int(char)) == int:
            return_msg += char
            
        else: #other special char will be omitted
            continue
        
    return return_msg


def main():
    while True:
        
        encript = input('Do you want to (e)ncrypt or (d)ecrypt? ').lower()
        while encript != 'e' and encript != 'd':
            try:
                encript = input('Choose between e or d to (e)ncrypt or (d)ecrypt: ').lower()    
            except:
                print('Wrong input, please read the question.\n')
                continue

        key_n = int(input('Please enter the key (0 to 25) to use: '))
        while key_n > 25 or key_n < 0:
            try:
                key_n = int(input('Please choose between 0 and 25.\n'))
            except ValueError:
                print('Invalid key. Please enter a valid integer.\n')
                continue

        msg = input('Enter the message to encrypt or decrypt: ')

        if encript == 'e':
            result = cypher(key_n, msg, True)
        else:
            result = cypher(key_n, msg, False)
        
        print('Result:', result)
        break  # Exit the loop after successful encryption/decryption

main()

'''
Explanation:

Creating the Alphabet Dictionary
alphabet_dict is a dictionary that maps each uppercase letter in the English alphabet to its corresponding index 
and vice versa. This is done using the string.ascii_uppercase method, which provides a string of all uppercase letters, 
and the enumerate() function, which provides an index to each letter as it is iterated over. 

cypher()
The cypher() function is the main function of this code. 

It accepts three arguments: 
1. key_n: the key to use for the encryption/decryption
2. msg: the message to be encrypted/decrypted
3. encript: a boolean indicating whether to encrypt (True) or decrypt (False)

The function first converts the message to uppercase. 
Then initializes an empty string, return_msg, which will hold the encrypted or decrypted message.

The function iterates over each character in the message. 
If the character is in the alphabet_dict, it is encrypted or decrypted. 
This is done by shifting the character's position in the alphabet by the key_n amount. 
The modulo operator % is used to ensure that the shift wraps around the alphabet, and the shifted character is then added to return_msg.

****side note about % operator****
% 26 is used after adding or subtracting the key number (key_n) to ensure that the resulting key stays within 
the range of 0 to 25, representing the indices of the alphabet. So, when encrypting a character, the code calculates 
the new key as (num + key_n) % 26. If the sum of num + key_n exceeds 25, the modulo operation ensures that the 
resulting key wraps around and starts from 0 again. And, when decrypting a character, the code calculates the new key 
as (num - key_n) % 26. If the difference of num - key_n becomes negative, the modulo operation ensures that the 
resulting key wraps around and starts from 25, counting backwards.
***********************************

If the character is a space or period, it is added to return_msg unchanged. 
If the character can be converted to an integer, it is also added to return_msg unchanged. 
Any other character (special characters, punctuation, etc.) is ignored.

The function finally returns the return_msg string, which contains the encrypted or decrypted message.


main()
The main() function is the entry point of this code. 
It prompts the user for the following inputs: 
1. whether they want to encrypt or decrypt a message
2. the key to use (an integer between 0 and 25)
3. the message to be encrypted/decrypted.

If the user inputs anything other than 'e' or 'd' for the encryption/decryption option, or a number outside of the 
range 0-25 for the key, the function will continue to prompt them until a valid input is received. 
This is done with the while loops

****side note on the while loops****
The main() function contains two while loops which serve as input validation mechanisms, ensuring that the 
user provides appropriate inputs to the program. the function iterates over the input until the correct options are
given by the user.
************************************

The function then calls the cypher() function with the appropriate arguments based on the user's inputs, 
and prints the result. Finally, it breaks out of the while loop, ending the program.



Finally... the call to main() at the end of the code is what starts the execution of the program.

'''