# davis burke, 20101583, 11/2/23
raw = input('What was your score?')
try:
    score =  float(raw)
except ValueError: 
    print('Insert a number please')
    quit()
try:
    if score >= 1.0:
        print('Input number between 0.1 and 1.0')
    elif score >= 0.9:
        print('A')
    elif score >= 0.8:
        print('B')
    elif score >= 0.7:
        print('C')
    elif score >= 0.6:
        print('D')
    elif score < 0.6:
        print('F')
except:
    print('Please enter a number between 0.1 and 1.0')
