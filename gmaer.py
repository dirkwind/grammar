# game file (hangman and Gorf)

import math, random, sys, time, string

from grammar_functions import *
from crunch import *

#---------------------------------------------Lists---------------------------------------------#

pronouns = ['he', 'she', 'I', 'you', 'we', 'y\'all', 'you guys']
verbs = ['cough', 'run', 'walk', 'defecate', 'flap', 'urinate', 'expunge', 'masticate', 'perambulate', 'touch', 'play', 'suck', 'pummel', 'open', 'spoon', 'dance', 'gorge', 'lunge', 'attack', 'jump', 'game end', 'game', 'yeet', 'clap', 'talk', 'stretch', 'work', 'swim', 'throw', 'insert', 'penetrate', 'rub', 'flex', 'slap', 'pet', 'milk', 'lick', 'call', 'prod', 'dwell', 'leap', 'strip', 'love', 'hate', 'despise', 'eat', 'fall', 'save', 'tend', 'raise', 'break', 'end', 'grow', 'obtain', 'wear', 'fight', 'fill', 'examine', 'replace', 'drink', 'hang', 'finish', 'escape', 'rid', 'adopt', 'pee', 'compact', 'ride', 'bite', 'burn', 'gibe', 'fertilize', 'vaporize', 'divorce', 'witness', 'choke', 'slam', 'ram', 'blow', 'drink', 'slurp', 'sip', 'forget', 'hurt', 'bend', 'mess', 'pay', 'see']
nouns = ['car', 'house', 'cat', 'skin', 'frog', 'desk', 'mom', 'tree', 'banana', 'orange', 'brother', 'sister', 'piano', 'fork', 'spoon', 'urinal', 'gas station bathroom', 'door', 'sink', 'fridge', 'hole', 'president', 'lap', 'sausage', 'boomer', '(nerf) gun', 'man', 'boy', 'baby', 'infant', 'woman', 'girl', 'toddler', 'child', 'grandpa', 'grandma', 'train', 'stomach', 'intestine', 'brain', 'foot', 'video game', 'gamer', 'phlegm', 'bush', 'toe', 'rump', 'teacher', 'pet', 'cow', 'pig', 'swine', 'milk', 'water', 'wheelchair', 'Fortnite', 'grum', 'grime', 'troglodyte', 'food', 'flask', 'urine', 'trash', 'leg', 'arm', 'rod', 'wood', 'morning', 'egg', 'seed', 'yolk', 'dwarf', 'chicken', 'clam', 'oyster', 'laser beam', 'buffoon', 'inquisition', 'emo', 'witness', 'hamster', 'national', 'jingo', 'mess']
adj = ['girthy', 'large', 'small', 'fat', 'tiny', 'ugly', 'hideous', 'unbelievable', 'lardful', 'bashful', 'dumb', 'sucky', 'presidential', 'erect', 'sad', 'colorful', 'stunning', 'lovely', 'open', 'obtuse', 'rowdy', 'jumbo', 'dapper', 'damp', 'wet', 'unpleasant', 'deplorable', 'barbarish', 'academic', 'unpleasant', 'broad', 'narrow', 'shy', 'high', 'damaged', 'dangerous', 'gluttonous', 'greedy', 'necrotic', 'relaxed', 'neurotic', 'paraplegic', 'epic', 'vile', 'putrid', 'abhorrent', 'adept', 'grimy', 'slimey', 'absurd', 'groggy', 'acidic', 'hefty', 'heinous', 'highfalautin', 'hot', 'spicey', 'exquisite', 'calamatous', 'loquacious', 'spastic', 'voracious', 'ravenous', 'zealous', 'saggy', 'hard', 'solid', 'slippery', 'catholic', 'edgy', 'derogatory', 'cretaceous', 'crustaceous', 'free']
loc = ["Applebee's", "Arby's", "Hardee's", "McDonald's", "Aldi", "Walmart", "Five Guys'", "In-N-Out Burger", "Lowe's", "Dick's Sporting Goods", "Kohl's", "school", 'the library', 'my house', 'Hot Topic', 'Ruler Foods', 'Meijer']
exclaim = ['zoinks', 'woah', 'wow', 'no way', 'what the heck', 'heck yeah', 'yay', 'hey', 'yo', 'uh oh', 'oh no', 'no', 'frick', 'epic', 'nice', 'alas', 'yum', 'um', 'ah', 'oh', 'aargh', 'ach', 'aha', 'boo-ya', 'oof', 'whew', 'yee-haw', 'golly', 'yikes', 'wowie', 'mmmm', 'ooh', 'yep', 'bah', 'ick', 'yuck', '*Coughs in Latin*']
names = ['Betty', 'Kromas', 'Larson', 'Johannes', 'Dogman', 'Krom', 'Mikey', 'Bob', 'Bill', 'Oprah', 'Logan', 'Karl', 'Karlie', 'Charlie', 'Jack', 'Mark', 'Tom', 'Jerry', 'Elizabeth', 'Sofia', 'Karen', 'Julius', 'Jane', 'Cromwell', 'Krista', 'Jeroboam', 'Jasmyn', 'Merlyn', 'Kolleen', 'Ira', 'Arlen', 'Yoel', 'Penelope', 'Graham', 'Iarfhlaith', 'Austen', 'Reagan', 'Norris', 'Oliver', 'Eugenio', 'Boaz', 'Chavaqquq', 'Daniyyel', 'Paulus', 'Rolf', 'Philip', 'Eutimio', 'Uilleag', 'Sergei', 'Zinovy', 'Galina', 'Katyusha', 'Vasili'] 

lists = [verbs, nouns, adj, exclaim, loc, names]



#---------------------------------------------Non-Gorf (functions)---------------------------------------------#

def word_count():
    total_words = 0
    for lis in lists: total_words += len(lis)
    print("\n\tVerbs:", len(verbs), "\n\tNouns:", len(nouns), '\n   Adjectives:', len(adj), '\nExclaimations:', len(loc), '\n\tNames:', len(names), '\n\n\tTotal:', total_words)

def hangman(word=None, guesses_to_lose=10):
    if word == None:
        word = random.choice(random.choice(lists))
    if word in verbs: print("\nThe word is a verb.")
    elif word in nouns: print("\nThe word is a noun.")
    elif word in adj: print("\nThe word is an adjective.")
    elif word in names: print("\nThe word is a name.")
    elif word in exclaim: print("\nThe word is an exclaimation.")
    elif word in loc: print("\nThe word is a location.")
    else: print("\nWord is unknown!")

    word = word.lower()
    playing = True
    spaced_word = ''
    right_word = ''.join([letter + ' ' for letter in word]) # this is the correct word in the s p a c e d  o u t format
    guesses = 0
    incorrect_letters = []
    correct_letters = []

    while playing:
        for letter in word:
            if letter == ' ': # if there is a space in a word
                spaced_word += '  '
            elif letter in ["'", "-", "*"]: # if the current letter is a special charater
                spaced_word += (letter + ' ')
                correct_letters.append(letter)
            elif letter in correct_letters: # if the letter has been correctly guessed
                spaced_word += (letter + " ")
            else: # if the letter has not been guessed
                spaced_word += "_ "

        print("\n" + spaced_word)

        if spaced_word == right_word: 
            print("\nThat is the word! You win!")
            return None
        
        spaced_word = ''

        guess = str(input("\nGuess a letter or word: "))

        if guess == word:
            print("\nThat is the word! Congratulations!")
            return None
        elif guess in word:
            print("\nThat is a letter!")
            correct_letters.append(guess)
        else:
            print("\nThat is not a letter in this word!")
            incorrect_letters.append(guess)
            guesses += 1
        
        if guesses == guesses_to_lose:
            print("\nOut of guesses, you lose! The word was '" + word + "'!")
            return None

        print("\nCorrectly Guessed Letters:", correct_letters)
        print("\nCorrectly Guessed Letters:", incorrect_letters)
        print("Wrong Guesses:", guesses, "/", guesses_to_lose)

#---------------------------------------------Gorf---------------------------------------------#

class Gorf(object):

    default_save_file = 'gorf_saves.txt'
    max_seed = 41

    def __init__(self, seed, seed_word, save_file=default_save_file):
        self.save_file = save_file
        if seed < 0 or seed > self.max_seed:
            self.seed = random.randint(0, self.max_seed)
        else:
            self.seed = seed
        if seed_word == False:
            print("\ngorf has been initialized with seed", str(self.seed) + ".")
        elif seed_word != False:
            print("\ngorf has been initialized with seed '" + str(seed_word) + "'.")

    
    
    #---------------Sentences---------------#

    def talk(self):
        if self.seed == 5:
            response = ("\nYou need to", random.choice(verbs), "on the", random.choice(nouns) + '.')
        elif self.seed == 6:
            response = ("\nYou are", add_a(random.choice(nouns)) + '.')
        elif self.seed == 0:
            response = ("\nYou", random.choice(verbs), 'and', random.choice(verbs), "with the", random.choice(nouns) + ".")
        elif self.seed == 1:
            response = ("\n" + add_a(random.choice(adj)).capitalize(), random.choice(nouns), plural(random.choice(verbs)) + ' with', add_a(random.choice(nouns)) + ".")
        elif self.seed == 2:
            response = ("\n" + random.choice(verbs).capitalize() + '.')
        elif self.seed == 3:
            response = ("\nYour", random.choice(nouns) + "'s", random.choice(adj), random.choice(nouns), "is absolutely", random.choice(adj) + ". I must", random.choice(verbs), "it.")
        elif self.seed == 4:
            response = ('\n' + add_a(random.choice(nouns)).capitalize(), plural(random.choice(verbs)), "you!")
        elif self.seed == 7:
            response = ('\nYour favorite noun is', random.choice(nouns) + '.')
        elif self.seed == 8:
            response = ('\nYou love it when', add_a(random.choice(adj)), random.choice(nouns), plural(random.choice(verbs)) + '.')
        elif self.seed == 9:
            response = ('\n'+ random.choice(verbs).capitalize(), add_a(random.choice(nouns)), 'for me.')
        elif self.seed == 11:
            response = ('\nGiving', add_a(random.choice(nouns)), add_a(random.choice(adj)), random.choice(verbs), "causes you to", random.choice(verbs) + ".")
        elif self.seed == 12:
            response = ('\nYou', random.choice(verbs), 'while', present(random.choice(verbs)), add_a(random.choice(adj)), random.choice(nouns) +'.')
        elif self.seed == 13:
            response = ('\nYou love to', random.choice(verbs), 'in public.')
        elif self.seed == 14:
            response = ("\nYou have", add_a(random.choice(adj)), 'desire to', random.choice(verbs), 'on the', random.choice(nouns) + "'s", random.choice(nouns) + ".")
        elif self.seed == 15:
            response = ("\n"+ random.choice(exclaim).capitalize()+"! I can't believe that", add_a(random.choice(adj)), random.choice(nouns), past(random.choice(verbs)), "at", random.choice(loc) + "!")
        elif self.seed == 16:
            response = ("\n" + random.choice(exclaim).capitalize()+"! The", random.choice(adj), random.choice(nouns), past(random.choice(verbs)), "on the", random.choice(nouns), "again.")
        elif self.seed == 17:
            response = ("\nThis", random.choice(nouns), "is so", random.choice(adj) + ".")
        elif self.seed == 18:
            response = ("\n" + random.choice(exclaim).capitalize()+"! I found this", random.choice(nouns), "in", add_a(random.choice(adj)), random.choice(nouns) +'.')
        elif self.seed == 19:
            response = ("\n" + add_a(random.choice(adj)).capitalize(), random.choice(nouns), 'is almost as bad as', add_a(random.choice(adj)), random.choice(nouns) + '.')
        elif self.seed == 20:
            response = ("\n" + random.choice(exclaim).capitalize() + "!", random.choice(names), 'just', past(random.choice(verbs)), "on the", random.choice(adj), random.choice(nouns) +'.')
        elif self.seed == 21:
            response = ("\nMy", present(random.choice(verbs)), random.choice(nouns) + '!', random.choice(exclaim).capitalize() + "!" )
        elif self.seed == 22:
            response = ("\n" + random.choice(exclaim).capitalize() + '!', random.choice(names), 'just', past(random.choice(verbs)) + '.')
        elif self.seed == 23:
            response = ("\nI wish", random.choice(names), 'would just', random.choice(verbs), 'on my', random.choice(nouns) + '.')
        elif self.seed == 24:
            response = ('\n'+random.choice(exclaim).capitalize() + "! I really want to", random.choice(verbs), "on", random.choice(names)+"'s", random.choice(adj), random.choice(nouns)+'.')
        elif self.seed == 25:
            response = ('\nYou are so', random.choice(adj)+',', random.choice(adj)+', and', random.choice(adj)+". I must", random.choice(verbs), 'on you.')
        elif self.seed == 26:
            response = ("\n"+ random.choice(exclaim).capitalize() + ", the", random.choice(nouns)+"!")
        elif self.seed == 27:
            response = ("\nThis", random.choice(nouns), "makes me really want to", random.choice(verbs), add_a(random.choice(nouns) + '.'))
        elif self.seed == 28:
            response = ("\n" + plural(random.choice(nouns)).capitalize(), "are", random.choice(adj) + '.')
        elif self.seed == 29:
            response = ("\nGuess what?", random.choice(verbs).capitalize(), "on my", random.choice([random.choice(nouns), plural(random.choice(nouns))]) + ".")
        elif self.seed == 30:
            response = ("\nYou are", random.choice(adj) + '.')
        elif self.seed == 31:
            response = ("\nHave you heard about the", random.choice(nouns) + '?')
        elif self.seed == 32:
            response = ("\n" + present(random.choice(verbs)).capitalize(), add_a(random.choice(adj)), random.choice(nouns), 'is considered', random.choice(nouns) + '-ist, you know.')
        elif self.seed == 33:
            response = ("\nMany", plural(random.choice(nouns)), 'are self-proclaimed "' + random.choice(nouns) + '-' + plural(nounify(random.choice(verbs))) +'".')
        elif self.seed == 34:
            response = ("\nYou are", add_a(present(random.choice(verbs))), random.choice(nouns) + '.')
        elif self.seed == 35:
            response = ("\nI wish you and I could", random.choice(verbs), 'together.')
        elif self.seed == 36:
            response = ("\nI would", random.choice(verbs), 'to', random.choice(verbs), random.choice(names), 'being', past(random.choice(verbs)) + '.')
        elif self.seed == 37:
            response = ("\nMy", random.choice(nouns), 'will be in your', random.choice(nouns), 'by the end of', random.choice(['the hour', 'this minute', 'today', 'the year', 'the decade', 'the century', 'this millennium']) + '.')
        elif self.seed == 38:
            response = ("\nMy", random.choice(['mom', 'dad', 'mother', 'father']), 'always told me, "When you\'re all out of', random.choice(nouns) + ', just go and', random.choice(verbs), 'your', random.choice(nouns) + '."')
        elif self.seed == 39:
            response = ('\n"' + plural(random.choice(nouns)).capitalize(), 'are the', plural(random.choice(nouns)), 'of', random.choice(adj), plural(random.choice(nouns)) + '." -', random.choice(['Barack Obama', 'Donald Trump', 'Abraham Lincoln', 'Bill Cosby', 'Hillary Clintin', 'Ronald Reagan', 'Winston Churchill', 'Beyonce', 'Lil Pump', '6ix 9ine', 'Drake', 'Kanye West', 'Brad Pitt', 'Ellen DeGeneres', 'Dwayne Johnson']) + '.')
        elif self.seed == 40:
            response = ("\nIf", add_a(random.choice(nouns)), plural(random.choice(verbs)) + ", it is", random.choice(adj), 'and', random.choice(adj) + '.')
        elif self.seed == 41: # f strings will be used from now on (older sentences might be converted later)
            response = (f"\nThe {random.choice(adj)} story is that {pronoun_possesive(random.choice(pronouns))} completely and utterly {random.choice(adj)}.")
        else:
            response = ("\nYou have to", random.choice(verbs) + '.')
        
        self.sentence = ''

        if type(response) != str:
            for section in response:
                self.sentence += section + ' '
        else:
            self.sentence = response
        
        print(self.sentence)

        self.seed = random.randint(0, self.max_seed)  
    
    def save_sentence(self):
        with open(self.save_file, 'a') as sf:
            sf.write(self.sentence)

    def get_saved_sentences(self):
        with open(self.save_file, 'r') as sf:
            data = sf.read()
        return data

    def erase_saved_data(self):
        with open(self.save_file, 'w') as sf:
            sf.write('')

#---------------------------------------------Execution---------------------------------------------#
    

def main(): # premade game using gorf and other functions
    # constants unique to main
    affirmations = ['yes', 'y', 'yeah', 'ye', 'ys', 'i do', 'indeed', 'affirmative', 'ok'] # any string that is considered a confirmation/approval

    #  initializing gorf
    start_word = None
    try:
        seed = int(input("Enter a seed: "))
    except ValueError:
        seed_word = ['egg', 'frog', 'oboe', 'tin', 'copper', 'lard', 'water', 'gamer', 'fortnite', 'time', 'log', 'wood', 'money', '$$$', 'dogma', 'cramp', 'bro', 'wheat', 'kyle']
        s_word = random.choice(seed_word)
        char_sum = 0
        for letter in s_word:
            char_sum += int(ord(letter))
        char_sum = abs(char_sum - (len(s_word) * 69 + 200))
        seed = char_sum

    gorf = Gorf(seed, start_word, 'saves/gorf_favs.txt')
    gorf.talk()
    using = True
    while using:
        user_input = str(input("\nDo you accept? ")).lower()
        if user_input in affirmations:
            gorf.talk()
        elif user_input == 'give':
            print('')
            main()
            using = False
        elif user_input == 'word':
            word_count()
        elif user_input == 'naughty':
            try:
                import naughty
                naughty.add_adj(adj)
                naughty.add_nouns(nouns)
                naughty.add_exclaim(exclaim)
                naughty.add_verbs(verbs)
                print("\nNaughty words have been added.")
            except:
                print("\nNice try, but the naughty file is not on your computer.")
        elif user_input in ['hang', 'hangman']:
            hangman()
        elif user_input in ['crunch', 'c']:
            crunch_word = input("\nEnter a word you want to crunch: ")
            print('\n', crunch(crunch_word))
        elif user_input in ['uncrunch', 'uc']:
            uncrunch_word = input("\nEnter a word you want to uncrunch: ")
            print('\n', uncrunch(uncrunch_word))
        elif user_input == 'save':
            try:
                gorf.save_sentence()
                print("\nSentence saved.")
            except:
                print("\nThere was an error while saving.")
        elif user_input == 'get saves':
            print(gorf.get_saved_sentences())
        elif user_input == 'erase saves':
            check = input("\nAre you sure that you want to erase your saves? (can't undo): ")
            if check.lower() in affirmations:
                gorf.erase_saved_data()
                print("\nData erased.")
        else:
            print('\ngorf is now sad\n')
            using = False

if __name__ == '__main__':
    main()