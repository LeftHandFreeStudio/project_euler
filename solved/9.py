def findPytTriplet():
	index = 1000
	a = list(range(1,1001))
	for i in a:
		toSplit = 1000 - i
		b = 0
		while b <= toSplit:
			c = toSplit - b
			if i**2 + b**2 == c**2:
				product = i*b*c
				print(i)
				print(b)
				print(c)
				return product
			b += 1

if __name__ == "__main__":
	print(findPytTriplet())		
