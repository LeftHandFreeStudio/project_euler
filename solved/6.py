def squareSum():
	numbers = list(range(1,101))
	squareSum = 0
	for i in numbers:
		squareSum += i**2
	sumNum = sum(numbers)
	sumNum = sumNum ** 2
	print(sumNum - squareSum)
if __name__ == "__main__":
	squareSum()		
