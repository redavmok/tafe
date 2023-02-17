#opens and reads file
text_file = open('romeo.txt', 'r')
text = text_file.read()

#cleans and strips the text
text = text.lower()
words = text.split()
words = [word.strip('.,!;()[]') for word in words]
words = [word.replace("'s", '') for word in words]

print(words)

#finds the unique words
unique = []
for word in words:
    if word not in unique:
        unique.append(word)

#sorts the words alphabetically
unique.sort()

print(unique)

