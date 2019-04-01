import math

lst = []

while True:
	try:
		x = str(input())
		lst.append(x.split())
	except EOFError:
		break

def calcp(n,k):
	pos = math.factorial(n) / (math.factorial(k)*math.factorial(n-k))
	return pos

plist = []
for people in lst:
	plist.append([calcp(int(people[0]),int(people[1])), people[2]])

plist.sort()

plist = plist[::-1]

ties = {}

for person in plist:

	if person[0] not in ties:
		ties[person[0]] = []

	ties[person[0]].append(person[1])

for group in ties:
	ties[group] = sorted(ties[group])[::-1]

result = []

for person in plist:

	if person[0] in ties:
		if ties[person[0]] == 1:
			result.append(person[1])
		else:
			result.extend(ties[person[0]])
			del ties[person[0]]

# print (result[::-1])

result = result[::-1]

i = 0
place = 0
val = 2

while 2**place < len(result):
	for x in range(2**place):

		if x != (2**place) -1:
			print(result[i], end = " ")
		else:
			print(result[i], end = "")

		i+=1
	place +=1
	print()


# print(plist)













		
