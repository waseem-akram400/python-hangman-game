alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
            'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']


def caesar(original_text, shift_amount, encode_or_decode):
    if encode_or_decode == "decode":
        shift_amount *= -1

    cipher_text = ""

    for letter in original_text:
        if letter in alphabet:
            shift_position = alphabet.index(letter) + shift_amount
            shift_position %= len(alphabet)
            cipher_text += alphabet[shift_position]
        else:
            cipher_text += letter

    print(f"Here is the {encode_or_decode}d result: {cipher_text}")


direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

caesar(original_text=text, shift_amount=shift, encode_or_decode=direction)