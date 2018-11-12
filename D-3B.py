import sys

encryptedFile = ""
sourceFile    = ""
isTerminated  = False
encValues     = ["a","b","c","d","e","f","g","h","i","j","A","B","C","D","G","H","I","J"]
i = 0

print "\n   [ * ] Simple 3xPinkyB Decrypter"

def __appUsage():
	print "   [ * ] Usage: python D-3B.py Test.java.3xPinkyB 12345678\n"
	print "   [ * ] Encryption Key Length Must be 8 and Must Be Numeric\n"

def __checkValidChar(charToBeChecked):
	z = 0
	isValidChar = False
	while z < len(encValues):
		if charToBeChecked == encValues[z]:
			isValidChar = True
		z = z + 1
	return isValidChar

def __calculateLastNumbers():
	global i, encryptedFile
	i = i + 1
	newVal = 0
	while (i < len(encryptedFile) and ord(encryptedFile[i]) >= 48 and ord(encryptedFile[i]) <= 57) or ord(encryptedFile[i]) == 10:
		if ord(encryptedFile[i]) != 10:
			newVal = (newVal * 10) + (ord(encryptedFile[i]) - 48)
		i = i + 1
	return newVal

def __checkASCIIValue(ASCIIValue):
	global sourceFile, isTerminated
	if ASCIIValue < 256 and ASCIIValue > 0:
		sourceFile = sourceFile + chr(ASCIIValue)
		isTerminated = False
	else:
		print "   [ * ] Invalid DeCryption Key Found Please Correct it" 
		__appUsage()
		isTerminated = True
		sourceFile = ""

def __checkChar(ch, fChar, sChar, tChar, foChar):
	if ch == fChar or ch == sChar or ch == tChar or ch == foChar:
		return True
	else:
		return False

if len(sys.argv) > 2:
	if len(str(sys.argv[2])) == 8:
		encKey      = str(sys.argv[2])    
		encKeyOne   = int(encKey[0] + encKey[1])
		encKeyTwo   = int(encKey[2] + encKey[3])
		encKeyThree = int(encKey[4] + encKey[5])
		encKeyFour  = int(encKey[6] + encKey[7])
		try:
			openFile = open(sys.argv[1],"r")
			encryptedFile = openFile.read()
			print "   [ * ] Please Wait While Decypting Source: " + sys.argv[1]
			while i < len(encryptedFile) and isTerminated == False:
				if encryptedFile[i] == "\\":
					if ord(encryptedFile[i + 1]) == 10:
						i = i + 1
						
					if encryptedFile[i + 1] == "e":
						i = i + 2
						ASCIIValue = 0
						while i < len(encryptedFile) and encryptedFile[i] != "\\" and isTerminated == False:
							isValidChar = __checkValidChar(encryptedFile[i])
							
							a = encryptedFile[i]
							if isValidChar == True:
								if __checkChar(encryptedFile[i],'a','A','I','i'):
									ASCIIValue = ASCIIValue + encKeyOne
									i = i + 1
								elif __checkChar(encryptedFile[i],'b','B','G','g'):
									ASCIIValue = ASCIIValue + encKeyTwo
									i = i + 1
								elif __checkChar(encryptedFile[i],'c','C','J','j'):
									ASCIIValue = ASCIIValue + encKeyThree
									i = i + 1
								elif __checkChar(encryptedFile[i],'d','D','H','h'):
									ASCIIValue = ASCIIValue + encKeyFour
									i = i + 1
								elif a == 'e':
									ASCIIValue = ASCIIValue + __calculateLastNumbers()
									__checkASCIIValue(ASCIIValue)
								elif a == 'f':
									ASCIIValue = ASCIIValue - __calculateLastNumbers()
									__checkASCIIValue(ASCIIValue)
							elif ord(a) == 10:
								i = i + 1
							else:
								isTerminated = True
								sourceFile = ""
								print "   [ * ] Please Insert a Valid Encrypted File Now Exiting"
								__appUsage()
								exit(0)
					elif encryptedFile[i + 1] == "~":
						sourceFile = sourceFile + "\n"
						i = i + 2
					elif encryptedFile[i + 1] == "*":
						sourceFile = sourceFile + chr(32)
						i = i + 2
					elif encryptedFile[i + 1] == "`":
						sourceFile = sourceFile + chr(9)
						i = i + 2
					elif ord(encryptedFile[i + 1]) == 10:
						i = i + 2
					else:
						i = len(encryptedFile)
						sourceFile = ""
						print "   [ * ] Please Insert a Valid Encrypted File Now Exiting"
						__appUsage()
						exit(0)
						isTerminated = True
				elif ord(encryptedFile[i]) == 10:
					i = i + 1
				else:
					i = len(encryptedFile)
					sourceFile = ""
					print "   [ * ] Please Insert a Valid Encrypted File Now Exiting"
					__appUsage()
					exit(0)
					isTerminated = True
			openFile.close()
			try:
				newFile = open(sys.argv[1] + ".DCRPT","w")
				newFile.write(sourceFile)
				newFile.close()
				print "   [ * ] Decrypted File Sucessfully Saved in File: " + sys.argv[1] + ".DCRPT\n"
			except IOError:
				print "   [ * ] Unable To Save Decrypted File\n"
		except IOError:
			print "   [ * ] Unable To Open File " + sys.argv[1] + "\n"
	else:
		print "   [ * ] Invalid Encryption Key Please Insert The Valid One"
		__appUsage()
		exit(0)
else:
	__appUsage()
	exit(0)
