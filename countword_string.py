name = input('Enter')
handle = open(name,'r')

count = dict()
for line in handle:
	words = line.split()
	for word in words:
		counts[word] = counts.get(word,0)+1

#find the most common word

bigcount = None
bigword = None
for word,count is counts.items():
	if bigcount is None or count> bigcount:
		bigword = word
		bigcount = count

print(bigword,bigcount)