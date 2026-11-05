# Morse Code Dictionary
MORSE_CODE = {
    # English Alphabet
    "A": ".-",    "B": "-...",  "C": "-.-.",
    "D": "-..",   "E": ".",     "F": "..-.",
    "G": "--.",   "H": "....",  "I": "..",
    "J": ".---",  "K": "-.-",   "L": ".-..",
    "M": "--",    "N": "-.",    "O": "---",
    "P": ".--.",  "Q": "--.-",  "R": ".-.",
    "S": "...",   "T": "-",     "U": "..-",
    "V": "...-",  "W": ".--",   "X": "-..-",
    "Y": "-.--",  "Z": "--..",

    # Numbers
    "0": "-----", "1": ".----", "2": "..---",
    "3": "...--", "4": "....-",  "5": ".....",
    "6": "-....", "7": "--...",  "8": "---..",
    "9": "----.",

    # Punctuation
    ".": ".-.-.-",
    ",": "--..--",
    "?": "..--..",
    "'": ".----.",
    "!": "-.-.--",
    "/": "-..-.",
    "(": "-.--.",
    ")": "-.--.-",
    "&": ".-...",
    ":": "---...",
    ";": "-.-.-.",
    "=": "-...-",
    "+": ".-.-.",
    "-": "-....-",
    "_": "..--.-",
    '"': ".-..-.",
    "$": "...-..-",
    "@": ".--.-."
}

# Reverse Dictionary
REVERSE_MORSE = {value: key for key, value in MORSE_CODE.items()}


def translator(text, mode):
    if mode:
        # Text -> Morse
        words = text.upper().split()
        return " / ".join(
            " ".join(MORSE_CODE.get(char, char) for char in word)
            for word in words
        )
    else:
        # Morse -> Text
        words = text.split(" / ")
        return " ".join(
            "".join(REVERSE_MORSE.get(code, "?") for code in word.split())
            for word in words
        )

def main():
    while True:
        menu = input(
            "1. Text - Morse\n"
            "2. Morse - Text\n"
            "3. Quit\n"
            "Choose: "
        )
        if menu == "1":
            text = input("\nEnter Something: ")
            print(f"\n>>> {translator(text, True)}\n")
        elif menu == "2":
            text = input("\nEnter Something: ")
            print(f"\n>>> {translator(text, False)}\n")
        elif menu == "3":
            break
        else:
            print("\n>> Invalid Input!\n")


if __name__ == "__main__":
    main()
    print("\n~ Thanks for choosing us ;)\n")
