# functions used for grammar
from copy import copy

# NOTE: variables that are ALL CAPS are to preserve the original cases of the characters in a variable

ignorecase_default = False
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

def config_upper(original_word: str, result: str, ignorecase: bool):
    '''Returns the configured result according to the parameters'''
    if original_word.isupper() and not ignorecase:
        return result.upper()
    elif ignorecase:
        return result.lower()
    return result

def config_ignorecase(ignorecase):
    '''Returns configured ignorecase base on ignorecase_default'''
    if ignorecase == 'bool':
        return ignorecase_default
    return ignorecase

def present(word: str, ignorecase='bool'):
    '''Returns the word in present tense (e.g. run --> running)
    \n\nword does not need to be a noun
    '''
    ignorecase = config_ignorecase(ignorecase)
    WORD = copy(word)
    word = word.lower()

    last_letter = word[len(word) - 1]
    scnd_last_letter = word[len(word) - 2]
    thrd_last_letter = word[len(word) - 3]
    result = None

    if in_exeptions(word, 'present'):
        result = grammar_exceptions[word]['present']
    elif last_letter == 'e' and scnd_last_letter in vowels:
        pass # pass means that it will return word + 'ing'
    elif last_letter == 'e' and scnd_last_letter != 'e':
        result = word[:len(word) - 1] + 'ing'
    elif last_letter == scnd_last_letter:
        pass
    elif thrd_last_letter == scnd_last_letter and last_letter not in vowels:
        pass
    elif thrd_last_letter in vowels and scnd_last_letter in vowels and last_letter not in vowels:
        pass
    elif scnd_last_letter in vowels and last_letter not in vowels and last_letter not in ['w', 'y']:
        result = WORD + last_letter + 'ing'
    if result is None:
        result = WORD + 'ing'

    return config_upper(WORD, result, ignorecase)

def past(word: str, ignorecase='bool'):
    '''Returns the past tense of a word (e.g. run --> ran)
    \n\nword does not need to be a verb
    '''
    ignorecase = config_ignorecase(ignorecase)
    WORD = copy(word)
    word = word.lower()

    last_letter = word[len(word) - 1]
    scnd_last_letter = word[len(word) - 2]

    if in_exeptions(word, 'past'):
        result = grammar_exceptions[word]['past']
    elif last_letter == 'e':
        result = WORD + 'd'
    elif scnd_last_letter in vowels and word[len(word) - 3] in vowels:
        result = WORD + 'ed'
    elif scnd_last_letter == 'e' and last_letter not in vowels:
        result = WORD[:len(word) - 2] + 'o' + last_letter
    elif scnd_last_letter in {'i', 'e'} and last_letter not in vowels:
        result = WORD[:len(word) - 2] + 'a' + last_letter
    elif last_letter not in vowels and scnd_last_letter not in vowels:
        result = WORD + 'ed'
    elif last_letter not in set(['e', 'i', 'o', 'u', 'y', 'a', 'k', 'x', 'h', 'w', 'd', 'y']):
        result = WORD + last_letter + 'ed'
    elif last_letter == 'y' and scnd_last_letter not in vowels:
        result = WORD[:len(word) - 1] + 'ied'
    else:
        result = WORD + 'ed' 
    
    return config_upper(WORD, result, ignorecase)
    
def plural(word: str, ignorecase='bool'):
    '''Returns the plural form of a word (e.g. run --> runs)
    \n\nword does not need to be a noun
    '''
    ignorecase = config_ignorecase(ignorecase)
    WORD = copy(word)
    word = word.lower()

    last_letter = word[len(word) - 1]
    scnd_last_letter = word[len(word) - 2]

    if in_exeptions(word, 'plural'):
        result = grammar_exceptions[word]['plural']
    elif last_letter == 'y' and scnd_last_letter not in vowels:
        result = WORD[:len(word) - 1] + 'ies'
    elif last_letter in {'h', 's'}:
        result = WORD + 'es'
    else:
        result = WORD + 's'
    
    return config_upper(WORD, result, ignorecase)

def nounify(word: str, ignorecase='bool'):
    '''Returns the noun version of a verb (e.g. run --> runner)
    \n\nthis will only work properly on verbs
    '''
    ignorecase = config_ignorecase(ignorecase)
    WORD = copy(word)
    word = word.lower()
    
    last_letter = word[len(word) - 1]

    if last_letter == 'e':
        result = WORD + 'r'
    elif last_letter != 'e' and word[len(word) - 2] not in vowels:
        result = WORD + 'er'
    else:
        result = WORD + last_letter + 'er'
    
    return config_upper(WORD, result, ignorecase)

def add_a(word: str, cap_a=False):
    '''Returns a word with the correct form of a in front of it (e.g. run --> a run)
    \n\ncap_a determines whether or not the 'a' or 'an' is capitalized
    '''
    WORD = copy(word)
    word = word.lower()

    if word[0] in vowels or word.startswith('herb'):
        a = 'an'
    else:
        a = 'a'
    
    if cap_a:
        a = a.capitalize()

    return a + ' ' + WORD

def pronoun_descriptive(pronoun: str, ignorecase='bool'):
    '''Returns pronoun followed by the correct descriptive verb (e.g. he --> he is)
    \n\nwill not work with words that are not pronouns
    '''
    ignorecase = config_ignorecase(ignorecase)
    PRONOUN = copy(pronoun)
    pronoun = pronoun.lower()

    if pronoun in ['she', 'he']:
        result = PRONOUN + ' is'
    elif pronoun == 'I':
        result = PRONOUN + ' am'
    else:
        result = PRONOUN + ' are'
    
    return config_upper(PRONOUN, result, ignorecase)

def pronoun_possessive(pronoun: str, ignorecase='bool'):
    '''Returns the possessive form of a prounoun (e.g. he --> his)'''
    ignorecase = config_ignorecase(ignorecase)

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
        return config_upper(pronoun, pronouns[pronoun.lower()], ignorecase)
    
# alternate function names
pron_desc = pronoun_descriptive
pron_poss = pronoun_possessive
ada = add_a