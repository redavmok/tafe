# this prints a list of the days emails are printed from, and counts how many

file_name = input('Enter name: ')
if len(file_name) < 1: file_name = 'mbox-short.txt'
handle = open(file_name)

# this block creates a dictionary to go line by line through the file
di = dict()
for line in handle:
# this if statement finds the email addresses, and skips the line if it's not the start of an email   
    if not line.startswith("From "):
        continue`
    else:
        line = line.rstrip()
        wds = line.split()
        word = wds[2]
        di[word] = di.get(word, 0) + 1
print(di)


