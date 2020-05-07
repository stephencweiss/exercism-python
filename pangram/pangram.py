def is_pangram(sentence):
    letters_present = set()
    for char in sentence:
        if char.isalpha():
            letters_present.add(str.lower(char))

    if len(letters_present) == 26:
        return True
    else:
        return False
