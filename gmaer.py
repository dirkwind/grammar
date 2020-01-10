import math, random, sys, time, string
from grammar_functions import *

#---------------------------------------------Lists and Dictionaries---------------------------------------------#



pronouns = ['he', 'she', 'I', 'you', 'we', 'y\'all', 'you guys']
verbs = ['cough', 'run', 'walk', 'defecate', 'flap', 'urinate', 'expunge', 'masticate', 'perambulate', 'touch', 'play', 'suck', 'pummel', 'open', 'spoon', 'dance', 'gorge', 'lunge', 'attack', 'jump', 'game end', 'game', 'yeet', 'clap', 'talk', 'stretch', 'work', 'swim', 'throw', 'insert', 'penetrate', 'rub', 'flex', 'slap', 'pet', 'milk', 'lick', 'call', 'prod', 'dwell', 'leap', 'strip', 'love', 'hate', 'despise', 'eat', 'fall', 'save', 'tend', 'raise', 'break', 'end', 'grow', 'obtain', 'wear', 'fight', 'fill', 'examine', 'replace', 'drink', 'hang', 'finish', 'escape', 'rid', 'adopt', 'pee', 'compact', 'ride', 'bite', 'burn', 'gibe', 'fertilize', 'vaporize', 'divorce', 'witness', 'choke', 'slam', 'ram', 'blow', 'drink', 'slurp', 'sip', 'forget', 'hurt', 'bend', 'mess', 'pay', 'see']
nouns = ['car', 'house', 'cat', 'skin', 'frog', 'desk', 'mom', 'tree', 'banana', 'orange', 'brother', 'sister', 'piano', 'fork', 'spoon', 'urinal', 'gas station bathroom', 'door', 'sink', 'fridge', 'hole', 'president', 'lap', 'sausage', 'boomer', '(nerf) gun', 'man', 'boy', 'baby', 'infant', 'woman', 'girl', 'toddler', 'child', 'grandpa', 'grandma', 'train', 'stomach', 'intestine', 'brain', 'foot', 'video game', 'gamer', 'phlegm', 'bush', 'toe', 'rump', 'teacher', 'pet', 'cow', 'pig', 'swine', 'milk', 'water', 'wheelchair', 'Fortnite', 'grum', 'grime', 'troglodyte', 'food', 'flask', 'urine', 'trash', 'leg', 'arm', 'rod', 'wood', 'morning', 'egg', 'seed', 'yolk', 'dwarf', 'chicken', 'clam', 'oyster', 'laser beam', 'buffoon', 'inquisition', 'emo', 'witness', 'hamster', 'national', 'jingo', 'mess']
adj = ['girthy', 'large', 'small', 'fat', 'tiny', 'ugly', 'hideous', 'unbelievable', 'lardful', 'bashful', 'dumb', 'sucky', 'presidential', 'erect', 'sad', 'colorful', 'stunning', 'lovely', 'open', 'obtuse', 'rowdy', 'jumbo', 'dapper', 'damp', 'wet', 'unpleasant', 'deplorable', 'barbarish', 'academic', 'unpleasant', 'broad', 'narrow', 'shy', 'high', 'damaged', 'dangerous', 'gluttonous', 'greedy', 'necrotic', 'relaxed', 'neurotic', 'paraplegic', 'epic', 'vile', 'putrid', 'abhorrent', 'adept', 'grimy', 'slimey', 'absurd', 'groggy', 'acidic', 'hefty', 'heinous', 'highfalautin', 'hot', 'spicey', 'exquisite', 'calamatous', 'loquacious', 'spastic', 'voracious', 'ravenous', 'zealous', 'saggy', 'hard', 'solid', 'slippery', 'catholic', 'edgy', 'derogatory', 'cretaceous', 'crustaceous', 'free']
loc = ["Applebee's", "Arby's", "Hardee's", "McDonald's", "Aldi", "Walmart", "Five Guys'", "In-N-Out Burger", "Lowe's", "Dick's Sporting Goods", "Kohl's", "school", 'the library', 'my house', 'Hot Topic', 'Ruler Foods', 'Meijer']
exclaim = ['zoinks', 'woah', 'wow', 'no way', 'what the heck', 'heck yeah', 'yay', 'hey', 'yo', 'uh oh', 'oh no', 'no', 'frick', 'epic', 'nice', 'alas', 'yum', 'um', 'ah', 'oh', 'aargh', 'ach', 'aha', 'boo-ya', 'oof', 'whew', 'yee-haw', 'golly', 'yikes', 'wowie', 'mmmm', 'ooh', 'yep', 'bah', 'ick', 'yuck', '*Coughs in Latin*']
names = ['Betty', 'Kromas', 'Larson', 'Johannes', 'Dogman', 'Krom', 'Mikey', 'Bob', 'Bill', 'Oprah', 'Logan', 'Karl', 'Karlie', 'Charlie', 'Jack', 'Mark', 'Tom', 'Jerry', 'Elizabeth', 'Sofia', 'Karen', 'Julius', 'Jane', 'Cromwell', 'Krista', 'Jeroboam', 'Jasmyn', 'Merlyn', 'Kolleen', 'Ira', 'Arlen', 'Yoel', 'Penelope', 'Graham', 'Iarfhlaith', 'Austen', 'Reagan', 'Norris', 'Oliver', 'Eugenio', 'Boaz', 'Chavaqquq', 'Daniyyel', 'Paulus', 'Rolf', 'Philip', 'Eutimio', 'Uilleag', 'Sergei', 'Zinovy', 'Galina', 'Katyusha', 'Vasili'] 

lists = [verbs, nouns, adj, exclaim, loc, names]



keys = {
    0: '\'?IUû!wK░@ÚÏrþ¢9MÍ<ukZ:G¹Óà³á║ÈÁHïÎÔoËY┼J╠╬┴0i3²7X▓í└┤ªºv¶÷yð,µjça©* ø2▄êâ.úTpÂ’ÖØý█1ÆóÌ´╔╦[Õæb$Òä“·«åtÑã§ëßì6+;s╝g£B&Lé”▒═{EîmO°¿ü-¼¥┬èÊö5╚%Çh¾»¤q╗Þc½^×ôÐ4]"}=Ä¦(¯`▀│fD├ÛWÝS─zÀd╩Å¨Ã#ñNC┐QnÜù8/¦®ÙF­¸¡\ÉAR)¬õÿxV|_■~òP>e±l╣',
    1: 'Ü×┼Úýæ]Z÷m±róz»¬╣êKú├wÉ³OªÇÍÛ╠╗ôÝ└BV1HdYg^Ó¶M­╬ï"vÁhX¨î>9¼┬¸ÿøÊxÄD│n´}(ET®kùIÒÆåÈûoÞc8áJsßÀí-ëqtÖ+Ð&”¦QØpÏã▀ò¥*G¯è©.05/²¿jLÂà¹$Ì§[)╚NWÙa¤Ã═3¢i°Î╝▄█Ñ{,\'`CÕ@Fä╦%A\Ô¡éâ?b4Uõ;ð#¦!<╔’|S2Rö6_░:=~■┐uË║ì7µ þ¾╩«f┤£Å·üPñ─▓º┴e▒“y½çl',
    2: 'Õcç4Ñöa\';├G8h"[+Kó½¥Îàÿ1±>ÖÌ£7 SÙ¾qÏÝåñá’┐i²NB*x!v~í╚âIj┬/k|¨¢Ø·ïÅäÃrÂÆp{]┼P╠ÐÞþÓôs╣=ì5¶&æ▒n³êÚ█│:D“ÄßÔZ╦µXÛAC©0øõ.▄,Ç»uúë×└¹░Ò▓╗«RzJ?$╔û§E_yOT¤tW¦═%éQÍ´Mè┤Àm2@Ul¯L\¼b¬dgH■îª╬#Ë°¸V`®”▀¡─ÊoF9)eã^}wº-ùòüðYf­╝Á6<║¿(ÜÈÉ¦÷╩┴3ý',
    3: '$╚┴})3╠ªgÚæ5"2a░óúeX¤│p▒’v┤Èy6ixSøÿç°Ò@ÔBEm*▓ï▄Î^=█²╬qu¦┐èl╦Ð¡ËÞ`R§oj¾&é7À¦-╗Í¹­º╣zQ íþîà~ZùwÁ>®ãA¿ÌÛ║{Ü4¬¸%N!ö/sL³nä├]µJÆÊ\▀¥(dÙM¨KØÇ.\'áåCUìÃrÑ:ûô╩ð«ß┬Å©Ä£Ö┼8|âõVP±GkÉñëY“╝1Óý└╔;t<¼■T+”─Ï¶×Âò,W_êüÕ¯¢[9hI´Fcb÷·?»½fH#Ý0═DO',
    4: '┼ºCÊ¦êï?Àd¾]╩}csJØ│F▒Î▀3·á╗■iÉG# wû<«┴¥½ÒeÆÄ$*|”þ¼ýµ§!^’NÌa,óÂ÷h"ú¶├Xôb╝K┤ä╣Üì└DA­Å=ñVÞ(øÑPül9;ß©ÍI┬HM─~═0ÐÁ{¯5╔EL╦ð╠¢¨¹³QÚx-q®>ù&gRj27WÇæ“Õf╬t╚²▄¸4nBÝèÓÈéò×░»▓Umk¡\':YZõÖÏ¿Ù¤█£T´@1/åí%yªàpÔ¦v[_)¬┐ëÛu°±\8║SçzoãO+`.â6îËÿÃör',
    5: '┼╦├ª/kËÑq7GÞæ1TÝ┴a´┤ê£┐.─Es╩ë¤ÛÇÉÓ9h)”M▒üâb└v█ÙÿñC~¿ZN³l▀Ö▄"OÁþÄ■╣o¬cD:»Ìº>d,¨P═iWASVû3║;ó¹j±©+╝ÐÅ®&¢LåúryÔ¼è5xØ“á{¸çù<õ╔¶Í=¾ÀY8▓Ã%┬·|Æ#öì6R Hà¦°^4Â¥g_¯2z\'0XµÒmôÎ«$IïF╚ä@ßUB([¡­-│píe½òt╗}Q÷\wÜÈn╠ãJuÏ░`Õ×îÚ²?¦K!ý╬*ø]ðfé’§Ê',
    6: 'éöÈÀ╩z`j“@Z_ÉQ█Ì\©þá&NêôG¸(®▄ã\'ð-§¬]╚fü¯æ°┐ûùu;K«╠»T#dú±PàYmº╬ÿ? ┴ÊÍ¶k┬Lò├ß╗õo:¹÷0£I╔.aqpí/S4,vËx²Øñ3w[▒ë▓║¿╦hE╣½¼▀Ã+µX·’}A7ÜD*8─C2s^FªÞ¥BMÓ"”Önì5Á<1çól┼´ÑÙRJåÄ└ÅrÏ¢)¦ÇÕ6by³Û░|Ôc│O┤HWâtUÝ=­ge¡¦╝¤!VÎèÚ$%{i~¾ýïÂÐ9×äÆÒ■î¨>ø═',
    7: '¤_bUÐhys½,Û©Lß\;ÔGWÅà^▒xÂj`*▄a¯|£╣dÉ4÷¼Oå¦▀Í6õºnô┴ip3¸ä!?ÿw=ïX1ùgø®’\'+f■P│├µ╗Ä█╦└[ãÃ×┬╝]âqz”ö▓æîì╬ÇòëRT¬ ­È«Üá┐─ú°ý┤Ë#¶-²Ql0§:.{Ú%þé“9$ñI/ü·ð)¦¢"Þ¹BVF}»êrÏ³╠2Ø¨ÎmÑ║Nv╔╩~Z¥oóû>uC¿ÌçM¾Õ╚èÀÝ´<±(Á&JEKtckAíÒÊÖ═┼░@¡HÙDÆ7S5ªY8Óe',
    8: '©.Rë╗Ø8Ýâ1▓OÚø²"iÖ`F═læºÆv┬Þ(+─┼”)s“¥ÕZáÙE@õd0¬╚Ó½;╬2 ±Ô|7ßnVù*Ï«à{þÄ║└LaWÇûr¹╔<¿pSò¡É┤:eå®X³Û▒´ó§Ðm¦­u]_j×Ã¸µ╠»▄├D╦£éôIP╣zTí!6HÈ¢Â&’?[=■,öãN~BêÌbC3g\$╩ï4ýy÷ä░c-^K┴▀│¤kèQ¯t·î\'Òðñü¼¾¨hÜÅç°fÊ┐Í}╝¶#UwÿÎÁì¦MÑúªJA59█x/YÀoq%ËG>',
    9: '¶{ae╔╚¦¦(Ï%ÇÅj#uW[À)Ö/¡Ìi¹pJõÒ"H║│Îwæ█A`5û<zcÓ7çßYM┤P├í¢´yÈÙò§½|èn×0Of▀êÜI▒Äà®v?ã¥­R┴·ÿ}rÚNþBböôØq┐hQ]²Ñ╬ñ╦KâS┼üÁ╗“*ù!▄~▓═’d¼8£Â└╩ú”@>23┬V_CËk-\:ÍîóÞ&©TÊìð¬¸ÃXá¯¾¨µ6x─«Eg;.░$ª+╣ÆlsD^t╠¤³ZÉÕäÔý■é±Gø÷=°¿F9╝om,U º\'ÐëÝ»Lïå4Û1'
}

alphabet = list('\'?IUû!wK░@ÚÏrþ¢9MÍ<ukZ:G¹Óà³á║ÈÁHïÎÔoËY┼J╠╬┴0i3²7X▓í└┤ªºv¶÷yð,µjça©* ø2▄êâ.úTpÂ’ÖØý█1ÆóÌ´╔╦[Õæb$Òä“·«åtÑã§ëßì6+;s╝g£B&Lé”▒═{EîmO°¿ü-¼¥┬èÊö5╚%Çh¾»¤q╗Þc½^×ôÐ4]"}=Ä¦(¯`▀│fD├ÛWÝS─zÀd╩Å¨Ã#ñNC┐QnÜù8/¦®ÙF­¸¡\ÉAR)¬õÿxV|_■~òP>e±l╣')

'''
thing = '!”’“"#$%&\'()*+,-./0123456789:;<=>?@ABCDEFGHIJKLMNOPQRSTUVWXYZ[\]^_`abcdefghijklmnopqrstuvwxyz{|}~¡¢£¤¥¦§¨©ª«¬­®¯°±²³´µ¶·¸¹º»¼½¾¿ÀÁÂÃÄÅÆÇÈÉÊËÌÍÎÏÐÑÒÓÔÕÖ×ØÙÚÛÜÝÞßàáâãäåæçèéêëìíîïðñòóôõö÷øùúûüýþÿ░▒▓│┤╣║╗╝┐└┴┬├─┼╚╔╩╦╠═╬█▄¦▀■'
res = ''
thing = list(thing)
print(len(thing))
for _ in range(0, 220):
    res = res + str(thing.pop(thing.index(random.choice(thing))))
print(res)
'''

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

def crunch(word):
    increment = 1
    result = ''
    try:
        alphabet = keys.get(int(word[0]))
    except:
        key = random.randint(0, 9)
        alphabet = list(keys.get(key))
        result = str(key)
    for letter in word:
        index = alphabet.index(letter) + increment
        index = index % len(alphabet)
        result += alphabet[index]
        increment *= 2
    return result

def uncrunch(word):
    result = ""
    increment = 1
    try:
        alphabet = keys.get(int(word[0]))
    except:
        key = random.randint(0, 9)
        alphabet = keys.get(key)
        result = str(key)
    for letter in word[1:]:
        index = alphabet.index(letter) - increment
        index = index % len(alphabet)
        result += alphabet[index]
        increment *= 2
    return result

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
        with open("saves/gorf_favs.txt", 'a') as save_file:
            save_file.write(self.sentence)

    def get_saved_sentences(self):
        with open('saves/gorf_favs.txt', 'r') as save_file:
            data = save_file.read()
        return data

    def erase_saved_data(self):
        with open('saves/gorf_favs.txt', 'w') as save_file:
            save_file.write('')

#---------------------------------------------Execution---------------------------------------------#
    

def main():
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
    test = str(input('choice: '))
    print(present(test))
    
    main()