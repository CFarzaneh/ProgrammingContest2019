from collections import deque

goal = str(input())
tree = str(input())

goal = goal.replace('(','')
goal = goal.replace(' ','')
goal = goal.replace(')','')

target = goal.split(',')[1]
start = goal.split(',')[0]

# print(target)
# print(start)

tree = tree.split('),')
tree = [x.replace('(','') for x in tree]
tree = [x.replace(')','') for x in tree]
tree = [x.replace(' ','') for x in tree]

# print(goal)
# print(tree)

hmap = {}

for entry in tree:
	pair = entry.split(",")

	if pair[0] not in hmap:
		hmap[pair[0]] = []

	hmap[pair[0]].append(pair[1])

# print(hmap)

paths = []

seen = set()



def findthepath(path,current,target,length,seen):

	if current == target:
		paths.append([path, length])
		return

	for child in hmap[current]:
		if child in seen or current in seen:
			continue
		else:
			seen.add(current)
			findthepath(path+" "+current, child, target,length+1,seen)

findthepath("",start,target,0,seen)

max_depth = max([x[1] for x in paths])

bestpaths = []

for path in paths:
	if path[1] == max_depth:
		letters = path[0].split()
		asci = 0
		for letter in letters:
			asci += ord(letter)

		bestpaths .append( [[asci, path]])

bestpaths.sort()

ans = bestpaths[0][0][1][0][1:]
ans = ans.replace(" ", ', ')
ans += ', '
ans += target
print(ans)
print(bestpaths[0][0][1][1])





