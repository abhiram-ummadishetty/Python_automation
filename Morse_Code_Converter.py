morse_code = {'A': "._", 'B': "_...", 'C': "_._.", 'D': "_..", 'E': ".", 'F': ".._.", 'G': "__.", 'H': "....",
              'I': "..", 'J': ".___", 'K': "_._", 'L': "._..", 'M': "__", 'N': "_.", 'O': "___", 'P': ".__.",
              'Q': "__._", 'R': "._.", 'S': "...", 'T': "_", 'U': ".._", 'V': "..._", 'W': ".__", 'X': "_.._",
              'Y': "_.__", 'Z': "__..", '0': "_____", '1': ".____", '2': "..___", '3': "...__", '4': "...._",
              '5': ".....", '6': "_....", '7': "__...", '8': "___..", '9': "____.", '.': "._._._", ',': "__..__",
              '?': "..__..", ' ': "/"}


# text to morse code
def textToMorse(text_input):
    cap_text = text_input.upper()
    # mapping the words to the above given morse code dictionery
    result = []
    for i in cap_text:
        result = map(lambda i: morse_code[i], cap_text)

    list_result = list(result)

    morse_text = " ".join(list_result)
    return morse_text


# morse code to text code
def morseToText(morse_input):
    word_array = morse_input.split("/")
    s = ""

    for i in word_array:
        letter = i.split(" ")
        for i in letter:
            for key, val in morse_code.items():
                if val == i:
                    s = s + key
        s = s + " "
    return s

