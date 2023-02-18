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
        word = wds[2]
        di[word] = di.get(word, 0) + 1

# largest = -1
# theword = None
# for k, v in di.items():
#         if v > largest:
#             largest = v
#             theword = k

print(di)