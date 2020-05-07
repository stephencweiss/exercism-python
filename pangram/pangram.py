def is_pangram(sentence):
    all_letters = set([char.lower() for char in sentence if char.isalpha()])
    return len(all_letters) == 26