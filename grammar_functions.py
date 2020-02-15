# functions used for grammar
from copy import copy

# NOTE: variables that are ALL CAPS are to preserve the original cases of the characters in a variable

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

def in_exeptions(word: str, tense: str):
    '''Checks if the provided word is in grammar_exceptions and if it contains an exception for the provided tense
    \n\ntenses are: 'past', 'plural', and 'present'
    '''
    word = word.lower()
    if word in grammar_exceptions:
        if tense in grammar_exceptions[word]:
            return True
    return False

def present(word: str):
    '''Returns the word in present tense (e.g. run --> running)
    \n\nword does not need to be a noun
    '''
    WORD = copy(word)
    word = word.lower()

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
        return WORD + last_letter + 'ing'
    return WORD + 'ing'
    

def past(word: str):
    '''Returns the past tense of a word (e.g. run --> ran)
    \n\nword does not need to be a verb
    '''
    WORD = copy(word)
    word = word.lower()

    last_letter = word[len(word) - 1]
    scnd_last_letter = word[len(word) - 2]

    if in_exeptions(word, 'past'):
        return grammar_exceptions[word]['past']
    elif last_letter == 'e':
        return WORD + 'd'
    elif scnd_last_letter in vowels and word[len(word) - 3] in vowels:
        return WORD + 'ed'
    elif scnd_last_letter == 'e' and last_letter not in vowels:
        return WORD[:len(word) - 2] + 'o' + last_letter
    elif scnd_last_letter in {'i', 'e'} and last_letter not in vowels:
        return WORD[:len(word) - 2] + 'a' + last_letter
    elif last_letter not in set(['e', 'i', 'o', 'u', 'y', 'a', 'k', 'x', 'h', 'w', 'd', 'y']):
        return WORD + last_letter + 'ed'
    elif last_letter == 'y' and scnd_last_letter not in vowels:
        return WORD[:len(word) - 1] + 'ied'
    else:
        return WORD + 'ed' 
    

def plural(word: str):
    '''Returns the plural form of a word (e.g. run --> runs)
    \n\nword does not need to be a noun
    '''
    WORD = copy(word)
    word = word.lower()

    last_letter = word[len(word) - 1]
    scnd_last_letter = word[len(word) - 2]

    if in_exeptions(word, 'plural'):
        return grammar_exceptions[word]['plural']
    elif last_letter == 'y' and scnd_last_letter not in vowels:
        return WORD[:len(word) - 1] + 'ies'
    elif last_letter in {'h', 's'}:
        return WORD + 'es'
    else:
        return WORD + 's'

def nounify(word: str):
    '''Returns the noun version of a verb (e.g. run --> runner)
    \n\nthis will only work properly on verbs
    '''
    WORD = copy(word)
    word = word.lower()
    
    last_letter = word[len(word) - 1]

    if last_letter == 'e':
        return WORD + 'r'
    elif last_letter != 'e' and word[len(word) - 2] not in vowels:
        return WORD + 'er'
    else:
        return WORD + last_letter + 'er'

def add_a(word: str):
    '''Returns a word with the correct form of a in front of it (e.g. run --> a run)'''
    WORD = copy(word)
    word = word.lower()

    if word[0] in vowels or word.startswith('herb'):
        return 'an ' + WORD
    else:
        return 'a ' + WORD

def pronoun_descriptive(pronoun: str):
    '''Returns pronoun followed by the correct descriptive verb (e.g. he --> he is)
    \n\nwill not work with words that are not pronouns
    '''
    PRONOUN = copy(pronoun)
    pronoun = pronoun.lower()

    if pronoun in ['she', 'he']:
        return PRONOUN + ' is'
    elif pronoun == 'I':
        return PRONOUN + ' am'
    else:
        return PRONOUN + ' are'

def pronoun_possessive(pronoun: str):
    '''Returns the possessive form of a prounoun (e.g. he --> his)'''
    pronouns = {
        'me': 'my',
        'i': 'my',
        'he': 'his',
        'she': 'her',
        'we': 'our',
        'you': 'your',
        'us': 'our'
    }
    if pronoun.lower() in pronouns:
        return pronouns[pronoun.lower()]