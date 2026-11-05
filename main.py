# English Alphabet
en_alphabet = "abcdefghijklmnopqrstuvwxyz"
morse_alphabet = [
    ".-",      # A
    "-...",    # B
    "-.-.",    # C
    "-..",     # D
    ".",       # E
    "..-.",    # F
    "--.",     # G
    "....",    # H
    "..",      # I
    ".---",    # J
    "-.-",     # K
    ".-..",    # L
    "--",      # M
    "-.",      # N
    "---",     # O
    ".--.",    # P
    "--.-",    # Q
    ".-.",     # R
    "...",     # S
    "-",       # T
    "..-",     # U
    "...-",    # V
    ".--",     # W
    "-..-",    # X
    "-.--",    # Y
    "--.."     # Z
]

# True -> (text - morse), False -> (morse - text)
def translator(t,b) :
    return " ".join(morse_alphabet[en_alphabet.index(i)] if i in en_alphabet else i for i in t) if b == True else  " ".join(en_alphabet[morse_alphabet.index(i)] if i in morse_alphabet else i for i in t.split())

def main() :
    while True :
        menu = input("1.Text - Morse\t2.Morse - Text\t3.Quit\n")
        if menu.isnumeric() :
            if menu == "1" :
                text = input("\nEnter Something : ")
                print(f"\n>>> {translator(text.strip().lower(),True)}\n")
            elif menu == "2" :
                text = input("\nEnter Something : ")
                print(f"\n>>> {translator(text.strip().lower(),False)}\n")
            elif menu == "3" : break
            else :
                print("\n>> Invalid Number !\n")
        else :
            print("\n>> Invalid Input !\n")

if __name__ == "__main__" :
    main()
    print("\n~ Thanks for choosing us ;)\n")