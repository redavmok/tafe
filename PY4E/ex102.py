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
        #print(wds)
        word = wds[5]
        splword = word.split(":")
        di[splword[0]] = di.get(splword[0], 0) + 1
# print(di)
# #print(di)

# #this block creates a tuple list from the dictionary, and sorts it highest to lowest
l = list()
for key,val in di.items():
    l.append((val,key))
l.sort(key=lambda a:a[1])

# #this block prints the most common email, and the count
for key, val in l:
    print(val,key)

