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
	

def checkPrime(n):
	half = 0
	prime = true
	if n%2 == 0:
		half = n/2
		return false
	else:
		half = (n-1)/2
	index = half
	while(index > 0):
		if n%index != 0:
			return false
		index -= 1
	return prime	
	


if __name__ == "__main__":
	number = 600851475143
	secNumb = 13195
	checkHighestPrimeFactor(number)
			
