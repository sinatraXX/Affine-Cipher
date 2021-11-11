import detectEnglish, cryptomath

SILENT_MODE = True

SYMBOLS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz'

def main():
	ciphertext = "yEZ BSSxOZ nxAEZm xf B YpAZ HS VHOHBcAEBuZYxn fRufYxYRYxHO nxAEZm, DEZmZ ZBnE cZYYZm xO BO BcAEBuZY xf VBAAZg YH xYf ORVZmxn ZtRxKBcZOY, ZOnmpAYZg RfxOL B fxVAcZ VBYEZVBYxnBc SROnYxHO, BOg nHOKZmYZg uBnj YH B cZYYZm."
	hackedMessage = hackAffine(ciphertext)

	if hackedMessage != None:
		print(hackedMessage)
	else:
		print('Failed to hack encryption.')

def getKeyParts(key):
	keyA = key // len(SYMBOLS)
	keyB = key % len(SYMBOLS)
	return (keyA, keyB)

def decryptMessage(key, ciphertext):
	keyA, keyB = getKeyParts(key)
	plaintext = ''
	modInverseOfKeyA = cryptomath.findModInverse(keyA,len(SYMBOLS))

	for letters in ciphertext:
		if letters in SYMBOLS:
			letterIndex = SYMBOLS.find(letters)
			plaintext += SYMBOLS[(letterIndex - keyB) * modInverseOfKeyA % len(SYMBOLS)]
		else:
			plaintext += letters
	return plaintext

def hackAffine(ciphertext):
	print('Hacking...')

	for key in range(len(SYMBOLS) ** 2):
		keyA = getKeyParts(key)[0]
		if cryptomath.gcd(keyA, len(SYMBOLS)) != 1:
			continue

		decryptedText = decryptMessage(key, ciphertext)

		if detectEnglish.isEnglish(decryptedText):
			print()
			print('Possible encryption hack: ')
			print('Key: %s' % (key))
			print('Decrypted message: ' + decryptedText[:300])
			print()
			print('Enter D for done, or just press Enter to continue hacking:')
			response = input('> ')

			if response.strip().upper().startswith('D'):
				return decryptedText
	return None

if __name__ == '__main__':
	main()

