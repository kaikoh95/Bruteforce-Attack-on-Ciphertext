from Crypto.Cipher import AES

#Function for padding the plaintext if it does not consist of 
#an integral number of 16-byte blocks
bs = AES.block_size
pad = lambda s: s + (bs - len(s) % bs) * chr(bs - len(s) % bs)

def KeyGen(keystring):
	"""Prints empty spaces and string length not more than 
	16 characters.
	"""

	key = keystring + " " * (16 - len(keystring))
	
	return key

def do_crypt(keystring):
	
	#Text to be modified
	intext = "This is a top secret." 
	
	#Generate key
	key = KeyGen(keystring)

	#Initialize the iv here
	iv = 16 * '\x00'
	
	#Initialize the encryption aes_128_cbc
	encryptor = AES.new(key, AES.MODE_CBC, iv)
	
	#Pad the plaintext
	text = pad(intext)

	ciphertext = encryptor.encrypt(text)
	
	#ciphertext in hex form
	ciphertext = ciphertext.hex()
	
	#Fill out the expected cipher text (can be modified)
	result = "8d20e5056a8d24d0462ce74e4904c1b5" + \
	         "13e10d1df4a2ef2ad4540fae1ca0aaf9"
	
	#Flag for exact match
	rightFlag = 1
	
	#Check whether the ciphertext matches with the result
	if result != ciphertext:
		rightFlag = 0

	if rightFlag == 1:
		return 100	
	
	return 1

if __name__ == '__main__':
	
	key = ""	
	outfile = "key.txt" #can be modified
	#Open the English word file
	with open('words.txt','r') as file:
		
		#For each word, check whether if the word 
		#contains less than 16-byte characters
		for keyword in file:
			keyword = keyword.strip()
		    
			#and use it as a key to see if the ciphertext matches
			if len(keyword) < 16 and do_crypt(keyword) == 100:
				key = keyword
				
	#Open file to be written
	out = open(outfile, "w")
	out.write("The key is: {}".format(key))
	out.close()	
	
				
	
