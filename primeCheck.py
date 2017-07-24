x= int(input('Enter an integer: '))
y= 1
is_prime=0

if x>10:
    if x%2!=0 and x%3!=0 and x%4!=0 and x%5!=0 and x%6!=0 and x%7!=0 and x%8!=0 and x%9!=0:
        is_prime=True
        print (is_prime)
    else:
        is_prime=False
        print (is_prime)
if x<=10:
    if x%y==0 and x%x==0:
        is_prime=True
        print (is_prime)
    else:
        is_prime=False
        print (is_prime)
