def find10001Prime():
	primes = [2]
	index = 3
	while len(primes) != 10001:
		print(len(primes))
		if checkPrime(index):
			primes.append(index)
		index += 2
	print(primes[-1])
	
def checkPrime(n):
	half = 0
	prime = True
	if n%2 == 0:
		half = n/2
		return False
	else:
		half = (n-1)/2
	
	index = half
	while(index > 1):
		if n%index == 0:
			prime = False
			break
		index -= 1
	return prime	
if __name__ == "__main__":
	find10001Prime()		
