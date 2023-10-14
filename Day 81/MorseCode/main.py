import strings

MORSE_DICT = {
    'A': '.-',     'B': '-...',   'C': '-.-.',   'D': '-..',    'E': '.',      'F': '..-.',   'G': '--.',
    'H': '....',   'I': '..',     'J': '.---',   'K': '-.-',    'L': '.-..',   'M': '--',     'N': '-.',
    'O': '---',    'P': '.--.',   'Q': '--.-',   'R': '.-.',    'S': '...',    'T': '-',      'U': '..-',
    'V': '...-',   'W': '.--',    'X': '-..-',   'Y': '-.--',   'Z': '--..',   '0': '-----',  '1': '.----',
    '2': '..---',  '3': '...--',  '4': '....-',  '5': '.....',  '6': '-....',  '7': '--...',  '8': '---..',
    '9': '----.',  '-': '-....-', '.': '.-.-.-', '!': '-.-.--', ',': '--..--', '?': '..--..', ':': '---...'
}

REVERSED_MORSE_DICT = {
    '.-': 'A',     '-...': 'B',   '-.-.': 'C',   '-..': 'D',    '.': 'E',      '..-.': 'F',   '--.': 'G',
    '....': 'H',   '..': 'I',     '.---': 'J',   '-.-': 'K',    '.-..': 'L',   '--': 'M',     '-.': 'N',
    '---': 'O',    '.--.': 'P',   '--.-': 'Q',   '.-.': 'R',    '...': 'S',    '-': 'T',      '..-': 'U',
    '...-': 'V',   '.--': 'W',    '-..-': 'X',   '-.--': 'Y',   '--..': 'Z',   '-----': '0',  '.----': '1',
    '..---': '2',  '...--': '3',  '....-': '4',  '.....': '5',  '-....': '6',  '--...': '7',  '---..': '8',
    '----.': '9',  '-....-': '-', '.-.-.-': '.', '-.-.--': '!', '--..--': ',', '..--..': '?', '---...': ':'
}

print(strings.welcome_message)

while True:
    choice = input("Choose an option (text2morse, morse2text, help, exit): ")

    if choice == 'text2morse':
        while True:
            text = input("Enter text to translate to morse ($ to exit): ")

            if text == '$':
                break

            morse = ""
            for letter in text:
                if letter == ' ':
                    morse = morse + "/ "
                else:
                    try:
                        morse = morse + MORSE_DICT[letter.upper()] + " "
                    except KeyError:
                        pass

            print("MORSE: " + morse)

    elif choice == 'morse2text':
        while True:
            morse = input("Enter morse to translate to text ($ to exit): ")

            if morse == '$':
                break

            text = ""
            for char in morse.split(' '):
                if char == '/':
                    text = text + " "
                else:
                    try:
                        text = text + REVERSED_MORSE_DICT[char]
                    except KeyError:
                        pass

            print("TEXT: " + text)

    elif choice == 'help':
        print(strings.help_message)

    elif choice == 'exit':
        print("Closing the application. Goodbye!")
        break

    else:
        print("Invalid choice! Please select a valid option.")
