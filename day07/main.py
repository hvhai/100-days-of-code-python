

logo = '''
 ██████╗███████╗ █████╗ ███████╗ █████╗ ██████╗      ██████╗██╗██████╗ ██╗  ██╗███████╗██████╗
██╔════╝██╔════╝██╔══██╗██╔════╝██╔══██╗██╔══██╗    ██╔════╝██║██╔══██╗██║  ██║██╔════╝██╔══██╗
██║     █████╗  ███████║███████╗███████║██████╔╝    ██║     ██║██████╔╝███████║█████╗  ██████╔╝
██║     ██╔══╝  ██╔══██║╚════██║██╔══██║██╔══██╗    ██║     ██║██╔═══╝ ██╔══██║██╔══╝  ██╔══██╗
╚██████╗███████╗██║  ██║███████║██║  ██║██║  ██║    ╚██████╗██║██║     ██║  ██║███████╗██║  ██║
 ╚═════╝╚══════╝╚═╝  ╚═╝╚══════╝╚═╝  ╚═╝╚═╝  ╚═╝     ╚═════╝╚═╝╚═╝     ╚═╝  ╚═╝╚══════╝╚═╝  ╚═╝
'''
print(logo)


def create_ceasar_cipher(mode, secret_message, shift):
    ''' This function creates a Caesar cipher that can encode or decode a message.
    '''
    # list of letters in the alphabet
    # and a dictionary to map letters to their index
    alphabet = list('abcdefghijklmnopqrstuvwxyz')
    alphabet_dict = {letter: index for index, letter in enumerate(alphabet)}
    # move the letters in the alphabet by the shift number
    encrypt_alphabet = alphabet[shift:] + alphabet[:shift]
    encrypt_alphabet_dict = {letter: index for index, letter in enumerate(encrypt_alphabet)}

    if mode == 'encode':
        new_position = [encrypt_alphabet_dict[letter] for letter in secret_message]
        encoded_message = [alphabet[position] for position in new_position]
        print(f'Encoded message: {''.join(encoded_message)}')
    elif mode == 'decode':
        new_position = [alphabet_dict[letter] for letter in secret_message]
        decoded_message = [encrypt_alphabet[position] for position in new_position]
        print(f'Decoded messaged: {''.join(decoded_message)}')
    else:
        print('Invalid mode. Please type "encode" or "decode".')


mode = input('Type "encode" to encrypt, type "decode" to decrypt:\n')
secret_message = list(input('Enter your message:\n').lower())
shift = int(input('Enter the shift number:\n'))
create_ceasar_cipher(mode, secret_message, shift)
