from collections import deque

hmap = {}

string = str(input())

entries = string.split(",")

target = entries[-1]

del entries[-1]

for entry in entries:
	values = entry.split("-")

	if values[0] not in hmap:
		hmap[values[0]] = []

	hmap[values[0]].append(values[1])


#print(hmap)

result = []

queue = deque()
queue.append([target,0])

level = 0

while len(queue) > 0:
	front = queue.popleft()

	if front[0] in hmap:
		for child in hmap[front[0]]:
			queue.append([child,front[1]+1])
	else:
		result.append(front)

max_depth = max([x[1] for x in result])


# print(result)

finalResult = []

for child in result:
	if child[1] == max_depth:
		finalResult.append(child[0])

finalResult.sort()

for x in finalResult:
	print(x,end='')

print()


	

