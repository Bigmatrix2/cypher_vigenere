import string

alphabet = string.printable + "éèêàôëùïü"

def cesar_cipher(message, key):

	crypted_message = ""
	for char in message:
		"""
		on va chiffrer le caractère 
			1- trouver la positon du carac dans l'alphabet
			2- y rajouter la clef à la positon du carac dans l'alphabet
			3- reccupérer le caractère chiffré
		on va stocker le caractère chiffrer
		"""
		index_carac_in_printable = alphabet.index(char)
		index_crypted_char = (index_carac_in_printable + key) % len(alphabet)
		cryted_char = alphabet[index_crypted_char]

		crypted_message += cryted_char
	
	return crypted_message


def cesar_uncipher(crypted_message, key):
	return cesar_cipher(crypted_message, -key)

crypted_message = cesar_cipher("salut les bgs aujourd'hui on va corriger l'exercice", 26)
print(crypted_message)

decrypted_message = cesar_uncipher("SALUTbLESbBGSbAUJOURD HUIbONbVAbCORRIGERbL EXERCICE", 26)
print(decrypted_message)

####################################################################################################################

def brute_force_cesar_cipher(crypted_message):
	for possible_key in range(0, len(alphabet)):
		print(cesar_uncipher(crypted_message, possible_key))
		print("_"*1)


brute_force_cesar_cipher(crypted_message)

#####################################################################################################################

def vigenere_cipher(message, password, reverse=False):
	list_of_keys = [alphabet.index(char) for char in password]
	crypted_message = ""
	
	for index, char in enumerate(message):
		current_key = list_of_keys[index % len(list_of_keys)]
		crypted_message += cesar_uncipher(char, current_key) if reverse else cesar_cipher(char, current_key)

	return crypted_message

crypted_message_2 = vigenere_cipher("salut les bgs aujourd'hui on va corriger l'exercice", "Hetic")
print(crypted_message_2)