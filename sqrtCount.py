#Asking for bounds
k= int(input('Enter first bound: '))
m= int(input('Enter second bound: '))

#Starting spots for calculation
q=0
i=0

#Counting mechanism
while (i*i)<=m:
    if i*i<k:
        i+=1
    if i*i>=k and i*i<=m:
        i+=1
        q+=1
print (q)

#Pause feature
input('\nPress ENTER to exit.')
