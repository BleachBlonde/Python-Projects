num = int(input('Enter number of players:'))
golf = open('golf.txt', 'w')
for i in range(1, num + 1):
   print (str('Enter name of player number ')+str(i)+str(':'))
   name = input()
   print (str('Enter score of player number ')+str(i)+str(':'))
   score = input()
   golf.write(name)
   golf.write('/n')
   golf.write(score)
   golf.write('/n')
