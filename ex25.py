def break_words(stuff):
    words = stuff.split(' ')
    return words

def sort_words(words):
    return sorted(words)

<<<<<<< HEAD
def print_first_word(words):
=======
def print_first_words(words):
    """Prints the first word after popping it off."""
>>>>>>> 5e04e943d2b3c959ea13eced8f11f7602a837f7b
    word = words.pop(0)
    print(word)

def sort_sentence(sentence):
    words = break_words(sentence)
    return sort_words(words)

def print_last_word(words):
<<<<<<< HEAD
    word = words.pop(-1)
    print(word)

def print_first_and_last(sentence):
=======
    """Prints the last word after popping it off."""
    word = words.pop(-1)
    print(word)

def sort_sentence(sentence):
    """Takes in a full sentence and returns the sorted words."""
    words = break_words(sentence)
    return sort_words(words)

def print_first_and_last(sentence):
    """Prints the first and last words of the sentence."""
>>>>>>> 5e04e943d2b3c959ea13eced8f11f7602a837f7b
    words = break_words(sentence)
    print_first_word(words)
    print_last_word(words)

def print_first_and_last_sorted(sentence):
    words = sort_sentence(sentence)
    print_first_word(words)
    print_last_words(words)


