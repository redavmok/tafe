# this code finds the most common email address that an email is sent from
file_name = input('Enter name: ')
if len(file_name) < 1: file_name = 'mbox-short.txt'
handle = open(file_name)
count = 0

di = dict()
for line in handle:
    if not line.startswith("From "):
        continue
    else:
        line = line.rstrip()
        wds = line.split()
        word = wds[1]
        count += 1
        countS = str(count)
        print(word)
print("There were " + countS + " lines in the file with From as the first word")

