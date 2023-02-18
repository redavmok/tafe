fhand = open('words.txt')
pie = dict()
total = 0
for line in fhand:
    word = line.strip()
    word2 = word.rstrip()
    word3 = word2.lower()
    pie[total] = word3
    total += 1
vals = list(pie.values())
print(pie)
if 'someone else solve a problem  this book assumes that' in vals:
    print('yes')
else:
    print('no')
