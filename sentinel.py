print ('This program is to help calculate grades.')
print ('Just enter your scores on assignments, when done enter stop.\n')

total = 0 
q = 0
score = ""

while score != "stop":
    score= input("Enter a score: ")
    if score!="stop":
        q += 1 
        total += int(score)
        avg = total / q
print('Your average is:', avg)

