import os
import re
import words as words


# GET_WORDS_LIST
#		/!\ nécessite l'import des modules os, re, words.py
#		Vérifie l'existence du fichier list.txt, le lit, formate les caractères à l'aide de words.py
#		Renvoie la liste de mots, sous la forme d'une liste de chaînes de caractères
def get_words_list():
	if not os.path.exists("list.txt"):
		raise SystemExit('Erreur: fichier de liste de mots introuvable.')
	file_list = open('list.txt', 'r', encoding="utf-8").readlines()
	res = list()
	for value in file_list:
		value = re.sub('\n', '', value)
		if words.match(value):
			value = words.format(value)
			res.append(value)
		else:
			raise SystemExit('Erreur: caractère non-prévu dans le fichier de liste de mots')
	return res

def display_begin(word_to_find, length_word):
	begin_display = list()
	begin_display.append(word_to_find[0])
	for i in range(1, length_word):
		begin_display.append(" ")
		begin_display.append("_")
	print(" ".join(begin_display))







