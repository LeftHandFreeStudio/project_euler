def findBiggest13LongProduct(name):
	data = readDocument(name)
	data = list(data)
	index = 0
	biggestSum = 0
	while index <= len(data) - 13:
		toSum = data[index:index + 13]
		summed = 1
		for i in toSum:
			summed *= eval(i)
		if summed > biggestSum:
			biggestSum = summed
		index += 1
	print(biggestSum)

		

def readDocument(name):
	with open(name, 'r') as number:
    		data=number.read().replace('\n', '')
	return data

if __name__ == "__main__":
	findBiggest13LongProduct("digits.txt")
