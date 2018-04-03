import fileinput

# lines = []
# for line in fileinput.input():
#    lines.append(line)

#for line in fileinput.input():
	#key, ref= (for val in line.split())

grammar = {}
check = []
def findNonTerminals(string):
	answer=""
	for name, arr in grammar.items():   
	    if string in arr:
	    	if name not in answer:
	        	answer= answer + name

	return answer

def findNonTerminalsFromArr(combinations):
	answer=""
	for string in combinations:
		for name, arr in grammar.items():   
		    if string in arr:
		    	if name not in answer:
		        	answer= answer + name

	return answer
def cleanString(word):
	answer=''
	for letter in word:
		if letter not in answer:
			answer+=letter

	return answer
def createMatrix(word):
	n = len(word)
	T = ['-'] * n
	for i in range(n):
	    T[i] = ['-'] * n
	return T	

def combinations(word1,word2):
	comb=[]
	for letter1 in word1:
		for letter2 in word2:
			conc = letter1+letter2
			if conc not in comb:
				comb.append(conc)
	return comb

def findNextNoEmpty(T,start,n):
	aux=''
	while(start<n):
		if(T[start][0]!=""):
			aux= T[start][0]
		start+=1
	return aux

def findNextNoEmptyDiagonal(T,start,n):
	aux=''
	while(start<n):
		if(T[start][start]!=""):
			aux= T[start][start]
		start+=1
	return aux

def CYK(T,word):
	n = len(word)
	for i in range(n):

		T[n-1][i] = findNonTerminals(word[i])

	for m in range(n-2,-1,-1):
		for i in range(0,m+1):
		
			if m==n-2:
				T[m][i]=findNonTerminalsFromArr(combinations(T[m+1][i],T[m+1][i+1]))
			elif m==0 and T[m+1][i] =="" and T[m+1][i+1]=="":
					aux =findNextNoEmpty(T,2,3)	
					aux2=findNextNoEmptyDiagonal(T,2,3)
					res = ''
					res+=findNonTerminalsFromArr(combinations(aux,aux2))
					T[m][i]=res

			else:
				answer=''
				answer+=findNonTerminalsFromArr(combinations(T[m+1][i],T[n-1][i+abs(m-(n-1))]))
				answer+=findNonTerminalsFromArr(combinations(T[m+1][i],T[n-2][i+abs(m-(n-1))]))
				answer+=findNonTerminalsFromArr(combinations(T[n-1][i],T[m+1][i+1]))
				T[m][i]=answer
	
 
	#print('\n'.join([' '.join(['{:4}'.format(item) for item in row]) 
     # for row in T]))

	start = list(grammar.keys())[0]
	if start in T[0][0]:
		print('Accepted')
	else:
		print('Rejected')

for line in fileinput.input():
	if(line[0].isupper()):
		key  = [val for val in line.split()]
		grammar[key[0]] = key[1:]
	else:
		check.append(line)
		
for word in check:
	T = createMatrix(word)
	CYK(T,word)










