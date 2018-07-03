def smallestEvenDivider():
	numbers = list(range(2,21))
	print(numbers)
	index = 20
	while(True):
		divisible = True
		for i in numbers:
			if index%i !=0:
				divisible = False
				break
		if divisible:
			print(index)
			break
		else:
			index += 20
			

if __name__ == "__main__":
	smallestEvenDivider()		
