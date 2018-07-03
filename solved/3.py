import itertools



def getCombinations(k,r,c):
	perms = []
	index = 0
	
def getPermutations(n):
	numbers = list(range(1,n +1))
	print(list(itertools.permutations(numbers, len(numbers))))

def checkHighestPrimeFactor(n):
	number = n
	index = 1
	while True:
		index += 1
		print(number)
		if index == number:
			print(number)
			break	
		while number%index == 0:
			number = number/index
		print(number)
	


if __name__ == "__main__":
	number = 600851475143
	secNumb = 13195
	checkHighestPrimeFactor(number)
			
