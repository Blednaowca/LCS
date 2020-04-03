import time

def LCS(stringA, stringB):
	la = len(stringA)
	lb = len(stringB)
	table = [[0 for x in range(lb + 1)]for y in range (la + 1)]
	
	for i in range(1,la + 1):
		for j in range(1,lb + 1):
			if(stringA[i - 1] == stringB[j - 1]):
				table[i][j] = table[i - 1][j - 1] + 1
			else:
				table[i][j] = max(table[i - 1][j], table[i][j - 1])
	for i in range(0,la):
		table[i+1][0] = stringA[i]
	return table

def MED(stringA, stringB):
	la = len(stringA)
	lb = len(stringB)
	table = [[1 for x in range(lb + 1)]for y in range (la + 1)]
	for i in range(0,la + 1):
		for j in range(0,lb + 1):
			if(i == 0):
				table[i][j] = j
			elif(j == 0):
				table[i][j] = i
			elif(stringA[i-1] == stringB[j-1]):
				table[i][j] = table[i - 1][j - 1]
			else:
				table[i][j]  = 1 + min(table[i - 1][j], table[i][j - 1], table[i - 1][j - 1])
	return table

def printTable(table):
	I = len(table)
	for i in range(I):
		print(table[i])

def recoverSequence(table):
	x = len(table) - 1
	y = len(table[0]) - 1
	sequence = ''
	while(x > 1 and y > 1):
		if (table[x - 1][y] < table[x][y]):
			if (table[x][y-1] < table[x][y]):
				sequence = table[x][0] + sequence
				x -= 1
				y -= 1
			else:
				y -= 1
		else:
			x -= 1
	while(x > 0):
		if (table[x - 1][y] < table[x][y]):
			sequence = table[x][0] + sequence
			return sequence
		else:
			x -= 1
	while(y > 0):
		if (isinstance(table[x][y - 1], str)):
			sequence = table[x][0] + sequence
			return sequence
		else:
			y -= 1
	return sequence

strings = [('ABCDGH', 'AEDFHR'),('AGGTAB', 'GXTXAYB'),('ABCBDAB', 'BDCABA'),('XMJYAUZ', 'MZJAWXU'),('sfeasafaasffsadgad','sfeasafaasffsadgad'),
			('ABCD', 'ACBAD'), ('asdfghjklasdfghjkl','lkjhgfdsaaasdfghjkl'), ('aaascaascaaaaaascaaaascaaaa', 'ascascascascasc'), 
			('zzzzzaabaaascdaasdaasdaddsfdasdfaasdfaasfeasafaasffsadgadfhaggfhagjaghjhghjijk', 'abcdefghijk')]

# w = LCS(*strings[5])
# printTable(w)
# print(recoverSequence(w))
# print(type(w[1][0]))
# print(isinstance(w[1][0], str))

for i in range(len(strings)):
	start = time.perf_counter_ns()
	LCS(*strings[i])
	end = time.perf_counter_ns()
	print(i, " pair took: ", (end - start) / 1000000, " ms")

print("MED time")

for i in range(len(strings)):
	start = time.perf_counter_ns()
	MED(*strings[i])
	end = time.perf_counter_ns()
	print(i ," pair took: ", (end - start) / 1000000, " ms")