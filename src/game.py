import words as words






# DISPLAY_CHAR_MATCH
#		Pour chaque lettre de word_a, vérifie sa présence et sa place dans word_b
#		Renvoie word_a sous la forme d'une chaine de caractères, avec () ou []
def display_char_match(word_a, word_b):
	list_a = list(word_a)
	list_b = list(word_b)
	res = list()
	
	for i in range(len(list_a)):
		char_a = list_a[i]
		if i < len(list_b):
			char_b = list_b[i]
		else:
			char_b = ""
		
		if char_a == char_b:
			res.append(str("[" + char_a + "]"))
		elif char_a in list_b:
			res.append(str("(" + char_a + ")"))
		else:
			res.append(str(" " + char_a + " "))
		res.append(" ")
	
	res.append("\n")
	return "".join(res)





# PLAYER_INPUT
#		/!\ nécessite l'import des modules words.py
#		Récupère l'input du joueur, vérifie s'il s'agit d'un mot de la bonne longueur
#		Renvoie le mot saisi, formatté à l'aide de words.py
def player_input(length, dictionary):
	incorrect_format = True
	while incorrect_format:
		guess = input(">")
		
		if not words.match(guess):
			print("\terreur: format incorrect")
		guess = words.format(guess)
		if not len(guess) == length:
			print("\terreur: longueur incorrecte")
		elif not is_word_in_dictionary(dictionary, guess):
			print("\terreur: mot inconnu")
		else:
			incorrect_format = False
	
	
	return guess

def is_word_in_dictionary(dictionary, word):
	word = word.upper()
	if word in dictionary:
		return True
	else:
		return False





