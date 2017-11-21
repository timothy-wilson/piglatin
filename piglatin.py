def translate_word(word):
    if word[:2]  in ['ch', 'sh', 'th']:
        i = 2
    else:
        i = 1
    fl = word[:i]
    translated = word
    if not fl in 'aeiou':
        translated = word[i:]
        translated += fl
    translated += 'ay'

    return translated


def translate(phrase):

    return ' '.join([translate_word(word) for word in phrase.split(' ')])


if __name__ == '__main__':
    import sys
    message = sys.argv[1]
    print(translate(message))
