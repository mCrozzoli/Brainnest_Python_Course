'''
This program can hack messages encrypted with the Caesar cipher from the previous project, even if you don’t know the key. There are only 26 
possible keys for the Caesar cipher, so a computer can easily try all possible decryptions and display the results to the user. In cryptography, we call this technique a brute-force attack.
'''

#!pip install PyEnchant

import string
import enchant

# Create an empty dictionary to store the alphabet mappings
alphabet_dict = {}

# Populate the dictionary with uppercase letters and their corresponding positions
for index, letter in enumerate(string.ascii_uppercase):
    alphabet_dict[letter] = index
    alphabet_dict[index] = letter


def cypher(key_n, msg, encript= True):
    """
    This function takes in a key and a message, and either encrypts or decrypts the message 
    using a simple Caesar cipher. The Caesar cipher works by shifting the letters of the 
    alphabet by a certain number of positions.
    
    Parameters:
    key_n (int): The number of positions to shift the alphabet by.
    msg (str): The message to encrypt or decrypt.
    encript (bool): Whether to encrypt (True) or decrypt (False) the message.
    
    Returns:
    return_msg (str): The encrypted or decrypted message.
    """
    
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


#check if the word is in a dictionary
def check_word(dictrionary, word):
    """
    This function checks if a word is in the provided dictionary.
    
    Parameters:
    dictrionary (dict): The dictionary to check the word against.
    word (str): The word to check.
    
    Returns:
    bool: True if the word is in the dictionary, False otherwise.
    """
    return dictrionary.check(word)


def brute_froce_decrypt(encripted_text, dictionary):
    """
    This function decrypts an encrypted message by trying all possible keys (from 0 to 25) in a Caesar cipher.
    It scores each decryption attempt by the number of decrypted words found in the provided dictionary.
    The decryption key that results in the highest score is considered the correct one.

    Args:
    encrypted_text (str): The text to be decrypted.
    dictionary (dict): The dictionary used to validate the decrypted words.
    """
    scores = {}
    
    for i in range(0,26):
        #encription set to False, so the cypher wil decript the msg
        decrypted_message = cypher(i,encripted_text,False) 
        
        #check the score of the message by comparing how many words of the decripted msg are in the distionary
        score = sum(1 for w in decrypted_message.split() if check_word(dictionary, w))
        scores[i] = score

    #get the key that has most words in the dictionary
    key_max_score = max(scores, key=scores.get)
    
    #decritped message with mosts words in the dictionary
    print(f"Key {key_max_score}: {cypher(int(key_max_score),encripted_text,False)}") 
            
        
def main():
    dictionary = enchant.Dict("en_US") #potentially the user can input language for decription
    encripted_msg = input('write the encripted message:' )
                          
    brute_froce_decrypt(encripted_msg, dictionary)

main()
    
    
'''
Report:

This Python script implements a brute force decryption method for text that has been encrypted using a Caesar cipher. A brute force method in the context of cryptography refers to an approach where an attacker systematically tries all possible keys to decrypt a ciphered text. In the case of a Caesar cipher, which shifts each letter in a message by a certain number of positions, the number of possible keys is equal to the number of letters in the alphabet - 26 for the English alphabet.

The main function of the script is brute_force_decrypt. This function takes in an encrypted message and a dictionary. The dictionary is used to validate whether the decrypted words are meaningful, as a successful decryption should result in a readable text.

The brute_force_decrypt function operates by iterating over all possible keys (0-25) and applying each one to the encrypted message. The decryption is done by the cypher function with the encryption flag set to False. For each key, the function counts how many words of the decrypted message are present in the provided dictionary. This is done by the check_word function. The key which results in the highest count (score) is considered to be the correct one, and the corresponding decrypted message is printed out.

The cypher function used within brute_force_decrypt is a simple implementation of a Caesar cipher that can both encrypt and decrypt messages. The check_word function is a helper function that checks the presence of a word in a given dictionary.
'''
    
    
    
    
    
    
    
    