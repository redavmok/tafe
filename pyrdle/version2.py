import random 

# this records all guessed words
almanac = list()
score = 100

## WORD LIST GENERATOR ##
file_name = input('Enter name of file: ')
if len(file_name) < 1:
    print("No input, program stopped.")
    exit()
else:   
#opens and reads file
    text_file = open(file_name)
    text = text_file.read()
#cleans and strips the text
    words = text.split()
    words = text.split("\n")
    words = [word.strip('.,!;()[]') for word in words]
    words = [word.replace("'s", '') for word in words]
    word_list = [word.upper() for word in words]

WORD = random.choice(word_list)

def score_guess(guess, WORD):
    count_total = 0
    count_misplaced_letters = len(missing_let)
    count_wrong_letters = len(wrong_let)*2
    count_total = (count_misplaced_letters + count_wrong_letters)
    return(count_total)


for guess_num in range(1,7):
    guess = input(f"\n{guess_num}:").upper()
    correct_let = {letter for letter, correct in zip(guess, WORD) if letter == correct}
    missing_let = set(guess) & set(WORD) - correct_let
    wrong_let = set(guess) - set(WORD)
    if len(guess) != 5:
        print("Error! Not 5 letters long!")
        continue
    else:
        almanac.append(guess)
        if guess == WORD:
            print("Correct!!")
            score -= score_guess(guess, WORD)
            break
        else:
            print("Wrong.")
            for char, letter in zip(WORD, guess):
                if letter in WORD and letter in char:
                    print(letter + " ✔ ")

                elif letter in WORD:
                    print(letter + " + ")
                else:
                    print(" X ")
            score -= score_guess(guess, WORD)


print(f"The word was {WORD}, you guessed {almanac}!")
print(f"Total score for this game was {score}/100." )


