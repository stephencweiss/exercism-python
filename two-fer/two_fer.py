def two_fer(name=''):
    sentence = ['One for ', 'you', ', one for me.']
    if name:
        sentence[1] = name
    return ''.join(sentence)
