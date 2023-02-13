# word = 'banana'
# count = 0
# for letter in word:
#     if letter == 'a':
#         count = count + 1
# print(count)


# def count(word, letter):
#     counter = 0
#     for character in word:
#         if character == letter:
#             counter += 1
#     return counter


# a = 'alphabet'
# b = 'a'

# x = count(a, b)

# print(x)

# fruit = 'banana'
# print(fruit.count('a'))

data = 'From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008'
atpos = data.find('@')
print(atpos)

sppos = data.find(' ',atpos)
print(sppos)

host = data[atpos+1:sppos]
print(host)
