MORSE_CODE_DICT = {
    'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 'F': '..-.', 'G': '--.', 'H': '....', 
    'I': '..', 'J': '.---', 'K': '-.-', 'L': '.-..', 'M': '--', 'N': '-.', 'O': '---', 'P': '.--.', 
    'Q': '--.-', 'R': '.-.', 'S': '...', 'T': '-', 'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-', 
    'Y': '-.--', 'Z': '--..',
    '1': '.----', '2': '..---', '3': '...--', '4': '....-', '5': '.....', '6': '-....', '7': '--...', 
    '8': '---..', '9': '----.', '0': '-----',
    '.': '.-.-.-', ',': '--..--', '?': '..--..', "'": '.----.', '!': '-.-.--', '/': '-..-.', '(': '-.--.', 
    ')': '-.--.-', '&': '.-...', ':': '---...', ';': '-.-.-.', '=': '-...-', '+': '.-.-.', '-': '-....-', 
    '_': '..--.-', '"': '.-..-.', '$': '...-..-', '@': '.--.-.', ' ': '/'
}

def english_to_morse(text):
    morse_code = ''
    for char in text.upper():
        if char in MORSE_CODE_DICT:
            morse_code += MORSE_CODE_DICT[char] + ' '
        else:
            morse_code += char
    return morse_code

def morse_to_english(morse_code):
    english_text = ''
    morse_code += ' ' # Adding extra space to detect end of a Morse code character
    char_in_morse = ''
    for char in morse_code:
        if char != ' ':
            char_in_morse += char
        else:
            if char_in_morse in MORSE_CODE_DICT.values():
                english_text += list(MORSE_CODE_DICT.keys())[list(MORSE_CODE_DICT.values()).index(char_in_morse)]
            else:
                english_text += char_in_morse
            char_in_morse = ''
    return english_text

if __name__ == "__main__":
    while True:
        print("Select translation direction:")
        print("1. English to Morse code")
        print("2. Morse code to English")
        print("3. Quit")
        choice = input("Enter your choice (1/2/3): ")

        if choice == '1':
            text = input("Enter the English text: ")
            morse_code = english_to_morse(text)
            print("Morse Code:", morse_code)
        elif choice == '2':
            morse_code = input("Enter the Morse code: ")
            english_text = morse_to_english(morse_code)
            print("English Text:", english_text)
        elif choice == '3':
            print("Exiting the program.")
            break
        else:
            print("Invalid choice. Please enter 1, 2, or 3.")
