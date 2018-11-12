# Simple Encryption Algorithm For TextFiles or SourceCodes
# It Only Works With ASCII Characters 
# Coded By 3xPinkyBlack(Habib Endris AJ)

# I am Not Responsible For any MisUse This Source Code or
# any Damage in any Way Please Use it Responsibly and For Education Purposes only
# Use it at Your Own Risk
import sys

encryptedFile = ""             # Variable To Assign The Encrypted File
sourceFile    = None		   # Source File To Be Encrypted
algChanger    = [0,0,0,0]      # Values To Change The Algorithm

# Special Strings Will Be Inserting In The Middle of Words and Letters
startString = "\e"      # Identifies The Starting of a Word
Space 		= "\*"      # Identifies Spaces Between Words
newLine 	= "\~"      # Identifies New Lines/End of Line 
tabLet 		= "\`"      # Identifies Tabs in One Line

print "\n   [ * ] Simple 3xPinkyB Encrypter"

def __appUsage():
	print "   [ * ] Usage: python E-3B.py Test.java 12345678\n"
	print "   [ * ] Encryption Key Length Must be 8 and Must be Numeric\n"

def __changeAlgForEncryption(ASCIIValue, encKeyNum, firstAlg, secondAlg):
	global algChanger, startString
	if algChanger[encKeyNum] == 0:
		newVal = startString + firstAlg + str(ASCIIValue)
		algChanger[encKeyNum] = 1
	else:
		newVal = startString + secondAlg + str(ASCIIValue)
		algChanger[encKeyNum] = 0
	return newVal

def __addToEncryptedFile(stringToBeAdded):
	global encryptedFile
	encryptedFile = encryptedFile + stringToBeAdded
	
if len(sys.argv) > 2:                              # Check if The Given Arguments are Greater Than 2 (eg): python E-3B.py fileName.txt encryptionKey
	if len(str(sys.argv[2])) == 8:
		encKey      = str(sys.argv[2])       
		encKeyOne   = int(encKey[0] + encKey[1])
		encKeyTwo   = int(encKey[2] + encKey[3])
		encKeyThree = int(encKey[4] + encKey[5])
		encKeyFour  = int(encKey[6] + encKey[7])
		EncLetValue = [encKeyOne,encKeyTwo,encKeyThree,encKeyFour]
		print "   [ * ] Please Save Your Encryption Key in A Safe Place --[" + sys.argv[2] + "]--"
		
		try:
			openFile = open(sys.argv[1],"r")		# Try To Open File Specified in The First Argument
			sourceFile = openFile.read()            # Read All The Contents of The Source File
			print "   [ * ] Please Wait Encypting Source: " + sys.argv[1]
			i = 0
			while i < len(sourceFile):                                   # Iterate Through The End of Source Text
				ASCIIValue = ord(sourceFile[i])							 # Get The ASCII Value of The Current Character
				newVal = ""
				if ASCIIValue == 32:                                     # If The ASCII Value is Space
					__addToEncryptedFile("\\*")
				elif ASCIIValue == 10: 									 # Else If The ASCII Value is New Line
					__addToEncryptedFile("\\~")
				elif ASCIIValue == 9:									 # Else If The ASCII Value is Tab
					__addToEncryptedFile("\\`")
				else:													 # Else The Above Conditions is Failed
					sumOne = EncLetValue[2] + EncLetValue[3] 
					if ASCIIValue >= sumOne:
						sumOne = sumOne + EncLetValue[0]
						if ASCIIValue >= sumOne:
							sumOne = sumOne + EncLetValue[1]
							if ASCIIValue >= sumOne:
								ASCIIValue = ASCIIValue - sumOne
								newVal = __changeAlgForEncryption(ASCIIValue,0,"DcGae","HcBie")
							else:
								ASCIIValue = sumOne - ASCIIValue
								newVal = __changeAlgForEncryption(ASCIIValue,1,"DJgaf","hcBif")
						else:
							ASCIIValue = sumOne - ASCIIValue
							newVal = __changeAlgForEncryption(ASCIIValue,2,"Hjaf","dJif")
					else:
						ASCIIValue = sumOne - ASCIIValue
						newVal = __changeAlgForEncryption(ASCIIValue,3,"DJf","jHf")
					__addToEncryptedFile(newVal)
				i = i + 1
			openFile.close()
			try:
				newFile = open(sys.argv[1] + ".3xPinkyB","a")
				y = 0
				while y < len(encryptedFile):
					if y >= 100:
						if y % 100 == 0:
							newFile.write("\n")
					newFile.write(encryptedFile[y])
					y = y + 1
				newFile.close()
				print "   [ * ] Encrypted File Sucessfully Saved in File: " + sys.argv[1] + ".3xPinkyB\n"
			except IOError:
				print "   [ * ] Unable To Save Encrypted File\n"
		except IOError:
			print "   [ * ] Unable To Open File " + sys.argv[1]
	else:
		print "   [ * ] Invalid Encryption Key Please Insert The Valid One"
		__appUsage()
		exit(0)
else:
	__appUsage()
	exit(0)
