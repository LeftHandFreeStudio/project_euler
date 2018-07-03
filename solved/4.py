
def findPalindrome():
	hiNum = 999*999
	possibleNumbers = list(range(100,1000))
	possibleNumbers = possibleNumbers[::-1]
	while hiNum > 0:
		if checkIfPalindrome(hiNum):
			for i in possibleNumbers:
				if hiNum%i == 0:
					if len(list(str(hiNum/i))) == 3:
						print(i)
						print(hiNum)
						return hiNum
			hiNum -=1
		else:
			hiNum -=1
	
def checkIfPalindrome(number):
	number = list(str(number))
	l = len(number)
	if l%2 == 0:
		l = l/2
		firstPart = number[:l]
		secondPart = number[l:]
		secondPart = secondPart[::-1]
		
		if(secondPart == firstPart):
			return True
		else:
			return False
	else:
		l = (l-1)/2
		firstPart = number[:l]
		secondPart = number[-l:]
		secondPart = secondPart[::-1]
		
		if(secondPart == firstPart):
			return True
		else:
			return False
		
		
		
if __name__ == "__main__":
	findPalindrome()
			
