import string
import random

english_frequencies = {'a': 8.167, 'b': 1.492, 'c': 2.782, 'd': 4.253, 'e': 12.702, 'f': 2.228, 'g': 2.015,
                       'h': 6.094, 'i': 6.966, 'j': 0.153, 'k': 0.772, 'l': 4.025, 'm': 2.406, 'n': 6.749, 'o': 7.507,
                       'p': 1.929, 'q': 0.095, 'r': 5.987, 's': 6.327, 't': 9.056, 'u': 2.758, 'v': 0.978, 'w': 2.360,
                       'x': 0.150, 'y': 1.974, 'z': 0.074}

def frequencyConstantEnglish(): 
    frequencyConstantEnglish = 0
    
    for letter, value in english_frequencies.items():
        frequencyConstantEnglish += value ** 2 

    return frequencyConstantEnglish

def frequencyConstant(input_text):
    input_text = input_text.lower()
    total_letters = 0
    letter_counts = {}

    # to count the occurrence of each letter in input text
    for letter in input_text:
        if letter.isalpha():
            total_letters += 1
            letter_counts[letter] = letter_counts.get(letter, 0) + 1

    # for each letter in the cipher text (letter_counts):
    #multiply its relative frequency in the text by its expected value in the English language (english_frequencies).
    #the result is added together to obtain the frequency constant.
    frequency_constant = sum((value / total_letters) * english_frequencies[letter] for letter, value in letter_counts.items())

    return frequency_constant

def encrypt_text(text, shift):
    text = text.lower()
    encrypted_text = ''
    
    for char in text:
        if char.isalpha():
            # encrypting with the specified shift
            shifted_char = chr((ord(char) - ord('a') + shift) % 26 + ord('a'))
            encrypted_text += shifted_char
        else:
        # keep the spaces
            encrypted_text += char

    return encrypted_text

def decrypt_and_find_best_shift(ciphertext):
    english_frequency_constant = frequencyConstantEnglish()

    best_decryption = ""
    best_frequency_constant_diff = float('inf')
    best_shift = 0

    #decrypting for each possible shift value
    for shift in range(26):
        decrypted_text = encrypt_text(ciphertext, shift)  # decryp the text using the current shift
        decrypted_frequency_constant = frequencyConstant(decrypted_text)  # calc the frequency constant

        #get the difference between the decrypted frequency constant and the English f.
        frequency_constant_diff = abs(decrypted_frequency_constant - english_frequency_constant)

        #set the best decryption if the current result is closer to the English 
        if frequency_constant_diff < best_frequency_constant_diff:
            best_frequency_constant_diff = frequency_constant_diff
            best_decryption              = decrypted_text
            best_shift                   = shift

    return best_decryption, best_shift

def generate_random_encrypted_text(original_text):
    random_shift = random.randint(1, 25)

    encrypted_text = encrypt_text(original_text, random_shift)

    return print('Encripted text:', encrypted_text,'\nShift:',random_shift)

def main():
    user_choice = input('Type what you want to do?\n1 - encrypt a text choosing the shift\n2 - decrypt a text\n3 - generate a random shift and cryoted text\n4 - Nothing\nYour option: ')

    if user_choice == '1':
        text = input('Type your text: ')
        shift = int(input('Shift: '))  # Convert user input to integer
        return print(encrypt_text(text, shift))
    if user_choice == '2':
        encrypted_message = input('Type your encripted text: ')
        decrypted_message, best_shift_used = decrypt_and_find_best_shift(encrypted_message)
        return print(f"Decrypted message: {decrypted_message}\nBest Shift Used: {best_shift_used}")
    if user_choice == '3':
        text = input('Type a text to be encrypted with a random shift: ')
        return generate_random_encrypted_text(text)
    if user_choice == '4':
        return 0

main()

#examplo of encrypted text to be used
#esp bftnv mczhy qzi ufxad zgpc esp wlkj ozr. estd td l nwlddtn dpyepynp fdpo qzc epdetyr pyncjaetzy lyo opncjaetzy lwrzctesxd. te nzyeltyd lww esp wpeepcd zq esp lwaslmpe lyo td l alyrclx. esp rzlw td ez pyncjae lyo espy opncjae estd dpyepynp htes l dstqe zq 4 lyo gpctqj tq esp acznpdd hzcvd nzccpnewj"

