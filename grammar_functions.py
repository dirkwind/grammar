# functions used for grammar

vowels = ['a', 'e', 'i', 'o', 'u']
grammar_exceptions = {
    #template: 'word' : {'plural' : '', 'past' : '', 'present' : ''},
    'run' : {'past' : 'ran'},
    'ride' : {'past' : 'rode'},
    'drink' : {'past' : 'drank'},
    'fight' : {'past' : 'fought'},
    'bring' : {'past' : 'brought'},
    'bite' : {'past' : 'bit'},
    'wear' : {'past' : 'wore'},
    'woman' : {'plural' : 'women'},
    'man' : {'plural' : 'men'}
}

def in_exeptions(word, tense):
    if word in grammar_exceptions:
        if tense in grammar_exceptions[word]:
            return True
    return False

def present(word):
    last_letter = word[len(word) - 1]
    scnd_last_letter = word[len(word) - 2]
    thrd_last_letter = word[len(word) - 3]

    if in_exeptions(word, 'present'):
        return grammar_exceptions[word]['present']
    elif last_letter == 'e' and scnd_last_letter in vowels:
        pass # pass means that it will return word + 'ing'
    elif last_letter == 'e' and scnd_last_letter != 'e':
        return word[:len(word) - 1] + 'ing'
    elif last_letter == scnd_last_letter:
        pass
    elif thrd_last_letter == scnd_last_letter and last_letter not in vowels:
        pass
    elif thrd_last_letter in vowels and scnd_last_letter in vowels and last_letter not in vowels:
        pass
    elif scnd_last_letter in vowels and last_letter not in vowels and last_letter not in ['w', 'y']:
        return word + last_letter + 'ing'
    return word + 'ing'
    

def past(word):
    last_letter = word[len(word) - 1]
    scnd_last_letter = word[len(word) - 2]

    if in_exeptions(word, 'past'):
        return grammar_exceptions[word]['past']
    elif last_letter == 'e':
        return word + 'd'
    elif scnd_last_letter in vowels and word[len(word) - 3] in vowels:
        return word + 'ed'
    elif scnd_last_letter == 'e' and last_letter not in vowels:
        return word[:len(word) - 2] + 'o' + last_letter
    elif scnd_last_letter in {'i', 'e'} and last_letter not in vowels:
        return word[:len(word) - 2] + 'a' + last_letter
    elif last_letter not in set(['e', 'i', 'o', 'u', 'y', 'a', 'k', 'x', 'h', 'w', 'd', 'y']):
        return word + last_letter + 'ed'
    elif last_letter == 'y' and scnd_last_letter not in vowels:
        return word[:len(word) - 1] + 'ied'
    else:
        return word + 'ed' 
    

def plural(word):
    last_letter = word[len(word) - 1]
    scnd_last_letter = word[len(word) - 2]

    if in_exeptions(word, 'plural'):
        return grammar_exceptions[word]['plural']
    elif last_letter == 'y' and scnd_last_letter not in vowels:
        return word[:len(word) - 1] + 'ies'
    elif last_letter in {'h', 's'}:
        return word + 'es'
    else:
        return word + 's'

def nounify(word):
    last_letter = word[len(word) - 1]

    if last_letter == 'e':
        return word + 'r'
    elif last_letter != 'e' and word[len(word) - 2] not in vowels:
        return word + 'er'
    else:
        return word + last_letter + 'er'

def add_a(word):
    if word[0] in vowels:
        return 'an ' + word
    else:
        return 'a ' + word

def pronoun_possesive(pronoun):
    if pronoun in ['she', 'he']:
        return pronoun + ' is'
    elif pronoun == 'I':
        return pronoun + ' am'
    else:
        return pronoun + ' are'