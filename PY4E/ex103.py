#opens and reads file
text_file = open('romeo.txt', 'r')
text = text_file.read()

#cleans and strips the text
text = text.lower()
words = text.split()
words = [word.strip('.,!;()[]') for word in words]
words = [word.replace("'s", '') for word in words]

unique = [i for ele in words for i in ele]
# print(unique)

# this block creates a dictionary of each letter and counts it
fdic = dict()
for char in unique:
        fdic[char[0]] = fdic.get(char[0], 0) + 1

# this block creates a tuple of each letter, and the number of times it appears
l = list()
for key,val in fdic.items():
    l.append((val,key))
l.sort(key=lambda a:a[1])
print(l)