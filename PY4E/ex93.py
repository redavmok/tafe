# this code finds the most common email address that an email is sent from
file_name = input('Enter name: ')
if len(file_name) < 1: file_name = 'mbox-short.txt'
handle = open(file_name)

di = dict()
for line in handle:
    if not line.startswith("From "):
        continue
    else:
        line = line.rstrip()
        wds = line.split()
        word = wds[1]
        di[word] = di.get(word, 0) + 1
#print(di)

bigcount = None
bigword = None
for word,count in di.items():
    if bigcount is None or count > bigcount:
        bigword = word
        bigcount = count
print(bigword, bigcount)