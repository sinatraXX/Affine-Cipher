# AFFINE CIPHER -- encrypt

# declare symbols that we're going to use [here i'm going to use letters only, both upper and lowercase]
SYMBOLS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz'

# declare the main function
def main():
  plaintext = "The affine cipher is a type of monoalphabetic substitution cipher, where each letter in an alphabet is mapped to its numeric equivalent, encrypted using a simple mathematical function, and converted back to a letter"
  theKey = 496
  translated = encryptMessage(theKey, plaintext)
  print(Key: %s' & (theKey))
  print(translated)
  
# this function is used to get the key parts
def getKeyParts(theKey):
  keyA = theKey // len(SYMBOLS)
  keyB = theKey % len(SYMBOLS)
  return(keyA, keyB)
  
# encryption
def encryptMessage(theKey, plaintext):
  keyA, keyB = getKeyParts(theKey)
  ciphertext = ''
  for letters in plaintext:
    if letters in SYMBOLS:
      letterIndex = SYMBOLS.find(letters)
      ciphertext += SYMBOLS[(letterIndex * keyA + keyB) % len(SYMBOLS)]
    else:
      ciphertext += letters
  return ciphertext
  
if __name__ == '__main__':
  main()
