# grammar
**THIS IS A WORK-IN-PROGRESS!** This is just a fun project I'm working on getting used to github and its workings. <br>
## What does grammar do?
Grammar contains a set of grammar function ([here](https://github.com/dirkwind/grammar/blob/master/grammar_functions.py "grammar_functions.py"))
and some custom encyption functions ([here](https://github.com/dirkwind/grammar/blob/master/crunch.py "crunch.py")).
The grammar functions convert a string into something that is grammatically correct (most of the time). For example if you say ```add_a("egg")```
it would return a string `an egg`. Both crunch and grammar_functions were originally made for [gmaer.py](https://github.com/dirkwind/grammar/blob/master/game/gmaer.py),
a "game" that generates random sentences based on specific templates, essentially madlibs.
## gmaer.py
gmaer.py contains a pre-made "game", hangman, and Gorf.
### The Pre-Made "Game"
The pre-made "game" is only ran when gmaer.py is ran directly. It uses the full potential of all that grammar has to offer, albeit in a weird way.
The user can use the crunch encryption, random sentence generator, and play hangman.
### Hangman
The hangman function takes a word and number of guesses as arguments. The user, as you can imagine, tries to guess the word or letters within it to win.
By default, the user gets seven guesses and the word is a random word from one of the word lists at the top of gmaer.py.
### Gorf
Gorf is a class that acts as a random sentence generator. It uses the word lists at the top of gmaer.py and preset templates to generate sentences.
It was designed with strange results in mind. Gorf also has the ability to save a generated sentence to a specified direectory. By default, this is `'gorf_saves.txt'`, which can be changed.
