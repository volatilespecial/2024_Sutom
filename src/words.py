import re



# MATCH
#		/!\ nécessite l'import du modules re
#		Vérifie si une chaine de caractères ne contient que les caractères acceptés
#		Renvoie un booléen
def match(char):
	if re.match('^[a-zA-ZàâäãåéèêëîïóôöûüçñæœÀÂÄÃÅÉÈÊËÎÏÓÔÖÛÜÇÑÆŒ]*$', char):
		return True
	else:
		return False


# FORMAT
#		/!\ nécessite l'import du modules re
#		Transforme une chaine de caractères et la renvoie en majuscules, sans accents
def format(word):
	word = word.upper()
	
	word = re.sub('[ÀÂÄÃÅ]', 'A', word)
	word = re.sub('[ÉÈÊË]', 'E', word)
	word = re.sub('[ÎÏ]', 'I', word)
	word = re.sub('[ÓÔÖ]', 'O', word)
	word = re.sub('[ÛÜ]', 'U', word)
	word = re.sub('[Ç]', 'C', word)
	word = re.sub('[Ñ]', 'N', word)
	
	word = re.sub('[Æ]', 'AE', word)
	word = re.sub('[Œ]', 'OE', word)
	
	return word


