import functools
inputNum = int(input())
games = {}

def mycmp(a, b):
	if a[1][0] !=  b[1][0]:
		return a[1][0]-b[1][0]
	if a[1][1] != b[1][1]:
		return a[1][1] - b[1][1]
	if a[1][2] != b[1][2]:
		return a[1][2] - b[1][2]
	if a[0] > b[0]:
		return 1
	else:
		return -1

	return 0


for x in range(inputNum):
	day = int(input())*-1
	stats = str(input())

	if x != (inputNum-1):
		newline = str(input())

	if day in games:
		stats = stats.split()
		stats = [int(x) for x in stats]
		games[day] = [games[day][0] + stats[0],games[day][1] + stats[1],games[day][2] + stats[2]]
	else:
		stats = stats.split()
		games[day] = [int(x) for x in stats]



lst = []

for game in games:
	lst.append([game , games[game]])

lst = sorted(lst,  key=functools.cmp_to_key(mycmp))[::-1]

for i in range(3):
	if i != 2:
		print(lst[i][0], end=" ")
	else:
		print(lst[i][0])


