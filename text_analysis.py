
# this code is licenced under creative commons licence as long as you 
# cite the author: Rene Pickhardt / www.rene-pickhardt.de 
 
# adds leading zeros to a string so all result strings can be ordered
def makeSortable(w):
	l = len(w)
	tmp = ""
	for i in range(5-l):
		tmp = tmp + "0"
	tmp = tmp + w
	return tmp
 
#replaces all kind of structures passed in l in a text s with the 2nd argument
def removeDelimiter(s,new,l):
	for c in l:
		s = s.replace(c, new);
	return s;
 
def analyzeWords(s):
	s = removeDelimiter(s," ",[".",",",";","_","-",":","!","?","\"",")","("])
	wordlist = s.split()
 
	dictionary = {}
	for word in wordlist:
		if word in dictionary:
			tmp = dictionary[word]
			dictionary[word]=tmp+1
		else:
			dictionary[word]=1
 
	l = [makeSortable(str(dictionary[k])) + " # " + k for k in dictionary.keys()]
 
	for w in sorted(l):
		print w
	count = {}
 
	for k in dictionary.keys():
		if dictionary[k] in count: 
			tmp = count[dictionary[k]]
			count[dictionary[k]] = tmp + 1
		else:
			count[dictionary[k]] = 1
	for k in sorted(count.keys()):
		print str(count[k]) + " words appear " + str(k) + " times"
 
def differentWords(s):
	s = removeDelimiter(s," ",[".",",",";","_","-",":","!","?","\"",")","("])
	wordlist = s.split()
	count = 0
	dictionary = {}
	for word in wordlist:
		if word in dictionary:
			tmp = dictionary[word]
			dictionary[word]=tmp+1
		else:
			dictionary[word]=1
			count = count + 1
	print str(count) + " different words"
	print "every word was used " + str(float(len(wordlist))/float(count)) + " times on average"	
	return count
 
 
def analyzeSentences(s):
	s = removeDelimiter(s,".",[".",";",":","!","?"])
	sentenceList = s.split(".")
	wordList = s.split()
	wordCount = len(wordList)
	sentenceCount = len(sentenceList)
	print str(wordCount) + " words in " + str(sentenceCount) + " sentences ==> " + str(float(wordCount)/float(sentenceCount)) + " words per sentence"	
 
	max = 0
	satz = ""
	for w in sentenceList:
		if len(w) > max:
			max = len(w);
			satz = w;
	print satz + "laenge " + str(len(satz))
 
texts = ["ulysses.txt","faust1.txt","faust2.txt"]
for text in texts:
	print text
	datei = open(text,'r')
	s = datei.read().lower()
	analyzeSentences(s)
	differentWords(s)
	analyzeWords(s)
	datei.close()

