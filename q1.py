numInput = int(input())

for x in range(numInput):
	words = str(input())

	words = words.split()

	max_num = 0
	max_char = ""

	if len(words[0]) != len(words[1]):
		print("#",end='')
		continue

	arr1 = [0]*128
	arr2 = [0]*128

	for i in range(len(words[0])):
		arr1[ord(words[0][i])] += 1
		if arr1[ord(words[0][i])] > max_num:
			max_num = arr1[ord(words[0][i])]
			max_char = words[0][i].upper()
		arr2[ord(words[1][i])] += 1

	booL = True
	for i in range(128):
		if arr1[i] != arr2[i]:
			print("#",end='')
			booL = False
			break

	if booL == True:
		print(max_char,end='')
	
print()







