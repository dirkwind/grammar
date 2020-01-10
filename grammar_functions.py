# functions used for grammar

vowels = ['a', 'e', 'i', 'o', 'u']
grammar_exceptions = {
    #template: 'word' : {'plural' : '', 'past' : '', 'present' : ''},
    'run' : {'plural' : 'runs', 'past' : 'ran', 'present' : 'running'},
    'play' : {'plural' : 'plays', 'past' : 'played', 'present' : 'playing'},
    'swim' : {'plural' : 'swims', 'past' : 'swam', 'present' : 'swimming'},
    'pet' : {'plural' : 'pets', 'past' : 'pat', 'present' : 'petting'},
    'ride' : {'plural' : 'rides', 'past' : 'rode', 'present' : 'riding'},
    'drink' : {'plural' : 'drinks', 'past' : 'drank', 'present' : 'drinking'},
    'fight' : {'plural' : 'fights', 'past' : 'fought', 'present' : 'fighting'},
    'bite' : {'plural' : 'bites', 'past' : 'bit', 'present' : 'biting'},
    'wear' : {'plural' : 'wears', 'past' : 'wore', 'present' : 'wearing'},
}

def present(word):
    last_letter = word[len(word) - 1]
    scnd_last_letter = word[len(word) - 2]
    thrd_last_letter = word[len(word) - 3]

    if last_letter == 'e' and scnd_last_letter != 'e':
        return word[:len(word) - 1] + 'ing'
    elif last_letter == scnd_last_letter:
        return word + 'ing'
    elif thrd_last_letter == scnd_last_letter and last_letter not in vowels:
        return word + 'ing'
    elif thrd_last_letter in vowels and scnd_last_letter in vowels and last_letter not in vowels:
        return word + 'ing'
    elif scnd_last_letter in vowels and last_letter not in vowels and last_letter not in ['w', 'y']:
        return word + last_letter + 'ing'
    else:
        return word + 'ing'
    

def past(word):
    last_letter = word[len(word) - 1]
    scnd_last_letter = word[len(word) - 2]

    if last_letter == 'e':
        return word + 'd'
    elif scnd_last_letter in vowels and word[len(word) - 3] in vowels:
        return word + 'ed'
    elif last_letter not in set(['e' 'i' 'o' 'u', 'y', 'a', 'k', 't', 'x', 'h', 'w', 'd', 'y']):
        return word + last_letter + 'ed'
    elif last_letter == 'y' and scnd_last_letter in vowels:
        return 
    elif last_letter == 'y':
        return word[:len(word) - 1] + 'ied'
    
    else:
        return word + 'ed' 
    

def plural(word):
    last_letter = word[len(word) - 1]
    scnd_last_letter = word[len(word) - 2]

    if last_letter == 'y' and scnd_last_letter not in vowels:
        return word[:len(word) - 1] + 'ies'
    elif last_letter == 'h':
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
        return 'an ' + str(word)
    else:
        return 'a ' + str(word)

def pronoun_possesive(pronoun):
    if pronoun in ['she', 'he']:
        return pronoun + ' is'
    elif pronoun == 'I':
        return pronoun + ' am'
    else:
        return pronoun + ' are'