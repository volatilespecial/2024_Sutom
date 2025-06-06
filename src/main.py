import startend as startend
import game as game
from art import *
import random

def main():
    tprint("SUTOM", font="random")
    print("Règles : si la lettre est entre [], elle est correcte et à la bonne place.\nSi la lettre est entre (), elle est correcte, mais n'est pas à la bonne place.\nUne lettre non correcte sera laissée telle quelle.\nVous avez 6 essais !\n")

    list_words = startend.get_words_list()
    word_to_find = random.choice(list_words)
    length_word = len(word_to_find)

    startend.display_begin(word_to_find, length_word)

    win = False

    for i in range(0,6):
        guess = game.player_input(length_word, list_words)
        if guess == word_to_find:
            print(game.display_char_match(guess, word_to_find))
            print("Vous avez trouvé le mot en",i+1,"essais !")
            win = True
            break
        else:
            print(game.display_char_match(guess, word_to_find))
    if not win:        
        print("Dommage ! Le mot était", word_to_find)

main()

