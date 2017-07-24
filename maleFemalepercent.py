males= int(input('Enter number of males:' ))
females= int(input('Enter number of females:' ))
percent_male= round((males/(males+females))*100)
percent_female= round((females/(males+females))*100)
print ('Percent males: ' + str(percent_male) + '%')
print ('Percent females: ' + str(percent_female) + '%')

input('\nPress ENTER to exit')
