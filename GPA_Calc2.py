#Revised College GPA Calculator
print ('GPA Calculator')
print ('created by Gaige Chester')
print ('\nPlease use only the values: a, b, c, d, or f.')
    
ask=input('\nHow many classes are you taking: ')
if ask=='13':
    grade1= input('\n\nEnter grade for first class: ')
    credit1= int(input('Enter credit hours for the class: '))
    if grade1=='a':
        grade1=4.0*credit1
    if grade1=='b':
        grade1=3.0*credit1
    if grade1=='c':
        grade1=2.0*credit1
    if grade1=='d':
        grade1=1.0*credit1
    if grade1=='f':
        grade1=0.0*credit1
        
    grade2=input('\nEnter grade for second class: ')
    credit2= int(input('Enter credit hours for the class:'))
    if grade2=='a':
        grade2=4.0*credit2
    if grade2=='b':
        grade2=3.0*credit2
    if grade2=='c':
        grade2=2.0*credit2
    if grade2=='d':
        grade2=1.0*credit2
    if grade2=='f':
        grade2=0.0*credit2
        
    grade3=input('\nEnter grade for third class: ')
    credit3= int(input('Enter credit hours for the class: '))
    if grade3=='a':
        grade3=4.0*credit3
    if grade3=='b':
        grade3=3.0*credit3
    if grade3=='c':
        grade3=2.0*credit3
    if grade3=='d':
        grade3=1.0*credit3
    if grade3=='f':
        grade3=0.0*credit3
            
    grade4=input('\nEnter grade for fourth class: ')
    credit4= int(input('Enter credit hours for the class: '))
    if grade4=='a':
        grade4=4.0*credit4
    if grade4=='b':
        grade4=3.0*credit4
    if grade4=='c':
        grade4=2.0*credit4
    if grade4=='d':
        grade4=1.0*credit4
    if grade4=='f':
        grade4=0.0*credit4
        
    grade5=input('\nEnter grade for fifth class: ')
    credit5= int(input('Enter credit hours for the class: '))
    if grade5=='a':
        grade5=4.0*credit5
    if grade5=='b':
        grade5=3.0*credit5
    if grade5=='c':
        grade5=2.0*credit5
    if grade5=='d':
        grade5=1.0*credit5
    if grade5=='f':
        grade5=0.0*credit5
        
    grade6=input('\nEnter grade for sixth class: ')
    credit6= int(input('Enter credit hours for the class: '))
    if grade6=='a':
        grade6=4.0*credit6
    if grade6=='b':
        grade6=3.0*credit6
    if grade6=='c':
        grade6=2.0*credit6
    if grade6=='d':
        grade6=1.0*credit6
    if grade6=='f':
        grade6=0.0*credit6

    grade7=input('\nEnter grade for seventh class: ')
    credit7= int(input('Enter credit hours for the class: '))
    if grade7=='a':
        grade7=4.0*credit7
    if grade7=='b':
        grade7=3.0*credit7
    if grade7=='c':
        grade7=2.0*credit7
    if grade7=='d':
        grade7=1.0*credit7
    if grade7=='f':
        grade7=0.0*credit7

    grade8=input('\nEnter grade for eighth class: ')
    credit8= int(input('Enter credit hours for the class: '))
    if grade8=='a':
        grade8=4.0*credit8
    if grade8=='b':
        grade8=3.0*credit8
    if grade8=='c':
        grade8=2.0*credit8
    if grade8=='d':
        grade8=1.0*credit8
    if grade8=='f':
        grade8=0.0*credit8

    grade9=input('\nEnter grade for ninth class: ')
    credit9= int(input('Enter credit hours for the class: '))
    if grade9=='a':
        grade9=4.0*credit9
    if grade9=='b':
        grade9=3.0*credit9
    if grade9=='c':
        grade9=2.0*credit9
    if grade9=='d':
        grade9=1.0*credit9
    if grade9=='f':
        grade9=0.0*credit9

    grade10=input('\nEnter grade for tenth class: ')
    credit10= int(input('Enter credit hours for the class: '))
    if grade10=='a':
        grade10=4.0*credit10
    if grade10=='b':
        grade10=3.0*credit10
    if grade10=='c':
        grade10=2.0*credit10
    if grade10=='d':
        grade10=1.0*credit10
    if grade10=='f':
        grade10=0.0*credit10

    grade11=input('\nEnter grade for eleventh class: ')
    credit11= int(input('Enter credit hours for the class: '))
    if grade11=='a':
        grade11=4.0*credit11
    if grade11=='b':
        grade11=3.0*credit11
    if grade11=='c':
        grade11=2.0*credit11
    if grade11=='d':
        grade11=1.0*credit11
    if grade11=='f':
        grade11=0.0*credit11

    grade12=input('\nEnter grade for twelveth class: ')
    credit12= int(input('Enter credit hours for the class: '))
    if grade12=='a':
        grade12=4.0*credit12
    if grade12=='b':
        grade12=3.0*credit12
    if grade12=='c':
        grade12=2.0*credit12
    if grade12=='d':
        grade12=1.0*credit12
    if grade12=='f':
        grade12=0.0*credit12

    grade13=input('\nEnter grade for thirteenth class: ')
    credit13= int(input('Enter credit hours for the class: '))
    if grade13=='a':
        grade13=4.0*credit13
    if grade13=='b':
        grade13=3.0*credit13
    if grade13=='c':
        grade13=2.0*credit13
    if grade13=='d':
        grade13=1.0*credit13
    if grade13=='f':
        grade13=0.0*credit13
        
    creditTotal= (credit1+credit2+credit3+credit4+credit5+credit6+credit7+credit8+credit9+credit10+credit11+credit12+credit13)
    gpa= float((grade1+grade2+grade3+grade4+grade5+grade6+grade7+grade8+grade9+grade10+grade11+grade12+grade13)/creditTotal)

    print ('\n\nYour current GPA is:',gpa)
    
if ask=='12':
    grade1= input('\n\nEnter grade for first class: ')
    credit1= int(input('Enter credit hours for the class: '))
    if grade1=='a':
        grade1=4.0*credit1
    if grade1=='b':
        grade1=3.0*credit1
    if grade1=='c':
        grade1=2.0*credit1
    if grade1=='d':
        grade1=1.0*credit1
    if grade1=='f':
        grade1=0.0*credit1
        
    grade2=input('\nEnter grade for second class: ')
    credit2= int(input('Enter credit hours for the class:'))
    if grade2=='a':
        grade2=4.0*credit2
    if grade2=='b':
        grade2=3.0*credit2
    if grade2=='c':
        grade2=2.0*credit2
    if grade2=='d':
        grade2=1.0*credit2
    if grade2=='f':
        grade2=0.0*credit2
        
    grade3=input('\nEnter grade for third class: ')
    credit3= int(input('Enter credit hours for the class: '))
    if grade3=='a':
        grade3=4.0*credit3
    if grade3=='b':
        grade3=3.0*credit3
    if grade3=='c':
        grade3=2.0*credit3
    if grade3=='d':
        grade3=1.0*credit3
    if grade3=='f':
        grade3=0.0*credit3
            
    grade4=input('\nEnter grade for fourth class: ')
    credit4= int(input('Enter credit hours for the class: '))
    if grade4=='a':
        grade4=4.0*credit4
    if grade4=='b':
        grade4=3.0*credit4
    if grade4=='c':
        grade4=2.0*credit4
    if grade4=='d':
        grade4=1.0*credit4
    if grade4=='f':
        grade4=0.0*credit4
        
    grade5=input('\nEnter grade for fifth class: ')
    credit5= int(input('Enter credit hours for the class: '))
    if grade5=='a':
        grade5=4.0*credit5
    if grade5=='b':
        grade5=3.0*credit5
    if grade5=='c':
        grade5=2.0*credit5
    if grade5=='d':
        grade5=1.0*credit5
    if grade5=='f':
        grade5=0.0*credit5
        
    grade6=input('\nEnter grade for sixth class: ')
    credit6= int(input('Enter credit hours for the class: '))
    if grade6=='a':
        grade6=4.0*credit6
    if grade6=='b':
        grade6=3.0*credit6
    if grade6=='c':
        grade6=2.0*credit6
    if grade6=='d':
        grade6=1.0*credit6
    if grade6=='f':
        grade6=0.0*credit6

    grade7=input('\nEnter grade for seventh class: ')
    credit7= int(input('Enter credit hours for the class: '))
    if grade7=='a':
        grade7=4.0*credit7
    if grade7=='b':
        grade7=3.0*credit7
    if grade7=='c':
        grade7=2.0*credit7
    if grade7=='d':
        grade7=1.0*credit7
    if grade7=='f':
        grade7=0.0*credit7

    grade8=input('\nEnter grade for eighth class: ')
    credit8= int(input('Enter credit hours for the class: '))
    if grade8=='a':
        grade8=4.0*credit8
    if grade8=='b':
        grade8=3.0*credit8
    if grade8=='c':
        grade8=2.0*credit8
    if grade8=='d':
        grade8=1.0*credit8
    if grade8=='f':
        grade8=0.0*credit8

    grade9=input('\nEnter grade for ninth class: ')
    credit9= int(input('Enter credit hours for the class: '))
    if grade9=='a':
        grade9=4.0*credit9
    if grade9=='b':
        grade9=3.0*credit9
    if grade9=='c':
        grade9=2.0*credit9
    if grade9=='d':
        grade9=1.0*credit9
    if grade9=='f':
        grade9=0.0*credit9

    grade10=input('\nEnter grade for tenth class: ')
    credit10= int(input('Enter credit hours for the class: '))
    if grade10=='a':
        grade10=4.0*credit10
    if grade10=='b':
        grade10=3.0*credit10
    if grade10=='c':
        grade10=2.0*credit10
    if grade10=='d':
        grade10=1.0*credit10
    if grade10=='f':
        grade10=0.0*credit10

    grade11=input('\nEnter grade for eleventh class: ')
    credit11= int(input('Enter credit hours for the class: '))
    if grade11=='a':
        grade11=4.0*credit11
    if grade11=='b':
        grade11=3.0*credit11
    if grade11=='c':
        grade11=2.0*credit11
    if grade11=='d':
        grade11=1.0*credit11
    if grade11=='f':
        grade11=0.0*credit11

    grade12=input('\nEnter grade for twelveth class: ')
    credit12= int(input('Enter credit hours for the class: '))
    if grade12=='a':
        grade12=4.0*credit12
    if grade12=='b':
        grade12=3.0*credit12
    if grade12=='c':
        grade12=2.0*credit12
    if grade12=='d':
        grade12=1.0*credit12
    if grade12=='f':
        grade12=0.0*credit12
        
    creditTotal= (credit1+credit2+credit3+credit4+credit5+credit6+credit7+credit8+credit9+credit10+credit11+credit12)
    gpa= float((grade1+grade2+grade3+grade4+grade5+grade6+grade7+grade8+grade9+grade10+grade11+grade12)/creditTotal)

    print ('\n\nYour current GPA is:',gpa)
    
if ask=='11':
    grade1= input('\n\nEnter grade for first class: ')
    credit1= int(input('Enter credit hours for the class: '))
    if grade1=='a':
        grade1=4.0*credit1
    if grade1=='b':
        grade1=3.0*credit1
    if grade1=='c':
        grade1=2.0*credit1
    if grade1=='d':
        grade1=1.0*credit1
    if grade1=='f':
        grade1=0.0*credit1
        
    grade2=input('\nEnter grade for second class: ')
    credit2= int(input('Enter credit hours for the class:'))
    if grade2=='a':
        grade2=4.0*credit2
    if grade2=='b':
        grade2=3.0*credit2
    if grade2=='c':
        grade2=2.0*credit2
    if grade2=='d':
        grade2=1.0*credit2
    if grade2=='f':
        grade2=0.0*credit2
        
    grade3=input('\nEnter grade for third class: ')
    credit3= int(input('Enter credit hours for the class: '))
    if grade3=='a':
        grade3=4.0*credit3
    if grade3=='b':
        grade3=3.0*credit3
    if grade3=='c':
        grade3=2.0*credit3
    if grade3=='d':
        grade3=1.0*credit3
    if grade3=='f':
        grade3=0.0*credit3
            
    grade4=input('\nEnter grade for fourth class: ')
    credit4= int(input('Enter credit hours for the class: '))
    if grade4=='a':
        grade4=4.0*credit4
    if grade4=='b':
        grade4=3.0*credit4
    if grade4=='c':
        grade4=2.0*credit4
    if grade4=='d':
        grade4=1.0*credit4
    if grade4=='f':
        grade4=0.0*credit4
        
    grade5=input('\nEnter grade for fifth class: ')
    credit5= int(input('Enter credit hours for the class: '))
    if grade5=='a':
        grade5=4.0*credit5
    if grade5=='b':
        grade5=3.0*credit5
    if grade5=='c':
        grade5=2.0*credit5
    if grade5=='d':
        grade5=1.0*credit5
    if grade5=='f':
        grade5=0.0*credit5
        
    grade6=input('\nEnter grade for sixth class: ')
    credit6= int(input('Enter credit hours for the class: '))
    if grade6=='a':
        grade6=4.0*credit6
    if grade6=='b':
        grade6=3.0*credit6
    if grade6=='c':
        grade6=2.0*credit6
    if grade6=='d':
        grade6=1.0*credit6
    if grade6=='f':
        grade6=0.0*credit6

    grade7=input('\nEnter grade for seventh class: ')
    credit7= int(input('Enter credit hours for the class: '))
    if grade7=='a':
        grade7=4.0*credit7
    if grade7=='b':
        grade7=3.0*credit7
    if grade7=='c':
        grade7=2.0*credit7
    if grade7=='d':
        grade7=1.0*credit7
    if grade7=='f':
        grade7=0.0*credit7

    grade8=input('\nEnter grade for eighth class: ')
    credit8= int(input('Enter credit hours for the class: '))
    if grade8=='a':
        grade8=4.0*credit8
    if grade8=='b':
        grade8=3.0*credit8
    if grade8=='c':
        grade8=2.0*credit8
    if grade8=='d':
        grade8=1.0*credit8
    if grade8=='f':
        grade8=0.0*credit8

    grade9=input('\nEnter grade for ninth class: ')
    credit9= int(input('Enter credit hours for the class: '))
    if grade9=='a':
        grade9=4.0*credit9
    if grade9=='b':
        grade9=3.0*credit9
    if grade9=='c':
        grade9=2.0*credit9
    if grade9=='d':
        grade9=1.0*credit9
    if grade9=='f':
        grade9=0.0*credit9

    grade10=input('\nEnter grade for tenth class: ')
    credit10= int(input('Enter credit hours for the class: '))
    if grade10=='a':
        grade10=4.0*credit10
    if grade10=='b':
        grade10=3.0*credit10
    if grade10=='c':
        grade10=2.0*credit10
    if grade10=='d':
        grade10=1.0*credit10
    if grade10=='f':
        grade10=0.0*credit10

    grade11=input('\nEnter grade for eleventh class: ')
    credit11= int(input('Enter credit hours for the class: '))
    if grade11=='a':
        grade11=4.0*credit11
    if grade11=='b':
        grade11=3.0*credit11
    if grade11=='c':
        grade11=2.0*credit11
    if grade11=='d':
        grade11=1.0*credit11
    if grade11=='f':
        grade11=0.0*credit11
        
    creditTotal= (credit1+credit2+credit3+credit4+credit5+credit6+credit7+credit8+credit9+credit10+credit11)
    gpa= float((grade1+grade2+grade3+grade4+grade5+grade6+grade7+grade8+grade9+grade10+grade11)/creditTotal)

    print ('\n\nYour current GPA is:',gpa)
    
if ask=='10':
    grade1= input('\n\nEnter grade for first class: ')
    credit1= int(input('Enter credit hours for the class: '))
    if grade1=='a':
        grade1=4.0*credit1
    if grade1=='b':
        grade1=3.0*credit1
    if grade1=='c':
        grade1=2.0*credit1
    if grade1=='d':
        grade1=1.0*credit1
    if grade1=='f':
        grade1=0.0*credit1
        
    grade2=input('\nEnter grade for second class: ')
    credit2= int(input('Enter credit hours for the class:'))
    if grade2=='a':
        grade2=4.0*credit2
    if grade2=='b':
        grade2=3.0*credit2
    if grade2=='c':
        grade2=2.0*credit2
    if grade2=='d':
        grade2=1.0*credit2
    if grade2=='f':
        grade2=0.0*credit2
        
    grade3=input('\nEnter grade for third class: ')
    credit3= int(input('Enter credit hours for the class: '))
    if grade3=='a':
        grade3=4.0*credit3
    if grade3=='b':
        grade3=3.0*credit3
    if grade3=='c':
        grade3=2.0*credit3
    if grade3=='d':
        grade3=1.0*credit3
    if grade3=='f':
        grade3=0.0*credit3
            
    grade4=input('\nEnter grade for fourth class: ')
    credit4= int(input('Enter credit hours for the class: '))
    if grade4=='a':
        grade4=4.0*credit4
    if grade4=='b':
        grade4=3.0*credit4
    if grade4=='c':
        grade4=2.0*credit4
    if grade4=='d':
        grade4=1.0*credit4
    if grade4=='f':
        grade4=0.0*credit4
        
    grade5=input('\nEnter grade for fifth class: ')
    credit5= int(input('Enter credit hours for the class: '))
    if grade5=='a':
        grade5=4.0*credit5
    if grade5=='b':
        grade5=3.0*credit5
    if grade5=='c':
        grade5=2.0*credit5
    if grade5=='d':
        grade5=1.0*credit5
    if grade5=='f':
        grade5=0.0*credit5
        
    grade6=input('\nEnter grade for sixth class: ')
    credit6= int(input('Enter credit hours for the class: '))
    if grade6=='a':
        grade6=4.0*credit6
    if grade6=='b':
        grade6=3.0*credit6
    if grade6=='c':
        grade6=2.0*credit6
    if grade6=='d':
        grade6=1.0*credit6
    if grade6=='f':
        grade6=0.0*credit6

    grade7=input('\nEnter grade for seventh class: ')
    credit7= int(input('Enter credit hours for the class: '))
    if grade7=='a':
        grade7=4.0*credit7
    if grade7=='b':
        grade7=3.0*credit7
    if grade7=='c':
        grade7=2.0*credit7
    if grade7=='d':
        grade7=1.0*credit7
    if grade7=='f':
        grade7=0.0*credit7

    grade8=input('\nEnter grade for eighth class: ')
    credit8= int(input('Enter credit hours for the class: '))
    if grade8=='a':
        grade8=4.0*credit8
    if grade8=='b':
        grade8=3.0*credit8
    if grade8=='c':
        grade8=2.0*credit8
    if grade8=='d':
        grade8=1.0*credit8
    if grade8=='f':
        grade8=0.0*credit8

    grade9=input('\nEnter grade for ninth class: ')
    credit9= int(input('Enter credit hours for the class: '))
    if grade9=='a':
        grade9=4.0*credit9
    if grade9=='b':
        grade9=3.0*credit9
    if grade9=='c':
        grade9=2.0*credit9
    if grade9=='d':
        grade9=1.0*credit9
    if grade9=='f':
        grade9=0.0*credit9

    grade10=input('\nEnter grade for tenth class: ')
    credit10= int(input('Enter credit hours for the class: '))
    if grade10=='a':
        grade10=4.0*credit10
    if grade10=='b':
        grade10=3.0*credit10
    if grade10=='c':
        grade10=2.0*credit10
    if grade10=='d':
        grade10=1.0*credit10
    if grade10=='f':
        grade10=0.0*credit10
        
    creditTotal= (credit1+credit2+credit3+credit4+credit5+credit6+credit7+credit8+credit9+credit10)
    gpa= float((grade1+grade2+grade3+grade4+grade5+grade6+grade7+grade8+grade9+grade10)/creditTotal)

    print ('\n\nYour current GPA is:',gpa)
    
if ask=='9':
    grade1= input('\n\nEnter grade for first class: ')
    credit1= int(input('Enter credit hours for the class: '))
    if grade1=='a':
        grade1=4.0*credit1
    if grade1=='b':
        grade1=3.0*credit1
    if grade1=='c':
        grade1=2.0*credit1
    if grade1=='d':
        grade1=1.0*credit1
    if grade1=='f':
        grade1=0.0*credit1
        
    grade2=input('\nEnter grade for second class: ')
    credit2= int(input('Enter credit hours for the class:'))
    if grade2=='a':
        grade2=4.0*credit2
    if grade2=='b':
        grade2=3.0*credit2
    if grade2=='c':
        grade2=2.0*credit2
    if grade2=='d':
        grade2=1.0*credit2
    if grade2=='f':
        grade2=0.0*credit2
        
    grade3=input('\nEnter grade for third class: ')
    credit3= int(input('Enter credit hours for the class: '))
    if grade3=='a':
        grade3=4.0*credit3
    if grade3=='b':
        grade3=3.0*credit3
    if grade3=='c':
        grade3=2.0*credit3
    if grade3=='d':
        grade3=1.0*credit3
    if grade3=='f':
        grade3=0.0*credit3
            
    grade4=input('\nEnter grade for fourth class: ')
    credit4= int(input('Enter credit hours for the class: '))
    if grade4=='a':
        grade4=4.0*credit4
    if grade4=='b':
        grade4=3.0*credit4
    if grade4=='c':
        grade4=2.0*credit4
    if grade4=='d':
        grade4=1.0*credit4
    if grade4=='f':
        grade4=0.0*credit4
        
    grade5=input('\nEnter grade for fifth class: ')
    credit5= int(input('Enter credit hours for the class: '))
    if grade5=='a':
        grade5=4.0*credit5
    if grade5=='b':
        grade5=3.0*credit5
    if grade5=='c':
        grade5=2.0*credit5
    if grade5=='d':
        grade5=1.0*credit5
    if grade5=='f':
        grade5=0.0*credit5
        
    grade6=input('\nEnter grade for sixth class: ')
    credit6= int(input('Enter credit hours for the class: '))
    if grade6=='a':
        grade6=4.0*credit6
    if grade6=='b':
        grade6=3.0*credit6
    if grade6=='c':
        grade6=2.0*credit6
    if grade6=='d':
        grade6=1.0*credit6
    if grade6=='f':
        grade6=0.0*credit6

    grade7=input('\nEnter grade for seventh class: ')
    credit7= int(input('Enter credit hours for the class: '))
    if grade7=='a':
        grade7=4.0*credit7
    if grade7=='b':
        grade7=3.0*credit7
    if grade7=='c':
        grade7=2.0*credit7
    if grade7=='d':
        grade7=1.0*credit7
    if grade7=='f':
        grade7=0.0*credit7

    grade8=input('\nEnter grade for eighth class: ')
    credit8= int(input('Enter credit hours for the class: '))
    if grade8=='a':
        grade8=4.0*credit8
    if grade8=='b':
        grade8=3.0*credit8
    if grade8=='c':
        grade8=2.0*credit8
    if grade8=='d':
        grade8=1.0*credit8
    if grade8=='f':
        grade8=0.0*credit8

    grade9=input('\nEnter grade for ninth class: ')
    credit9= int(input('Enter credit hours for the class: '))
    if grade9=='a':
        grade9=4.0*credit9
    if grade9=='b':
        grade9=3.0*credit9
    if grade9=='c':
        grade9=2.0*credit9
    if grade9=='d':
        grade9=1.0*credit9
    if grade9=='f':
        grade9=0.0*credit9
        
    creditTotal= (credit1+credit2+credit3+credit4+credit5+credit6+credit7+credit8+credit9)
    gpa= float((grade1+grade2+grade3+grade4+grade5+grade6+grade7+grade8+grade9)/creditTotal)

    print ('\n\nYour current GPA is:',gpa)
    
if ask=='8':
    grade1= input('\n\nEnter grade for first class: ')
    credit1= int(input('Enter credit hours for the class: '))
    if grade1=='a':
        grade1=4.0*credit1
    if grade1=='b':
        grade1=3.0*credit1
    if grade1=='c':
        grade1=2.0*credit1
    if grade1=='d':
        grade1=1.0*credit1
    if grade1=='f':
        grade1=0.0*credit1
        
    grade2=input('\nEnter grade for second class: ')
    credit2= int(input('Enter credit hours for the class:'))
    if grade2=='a':
        grade2=4.0*credit2
    if grade2=='b':
        grade2=3.0*credit2
    if grade2=='c':
        grade2=2.0*credit2
    if grade2=='d':
        grade2=1.0*credit2
    if grade2=='f':
        grade2=0.0*credit2
        
    grade3=input('\nEnter grade for third class: ')
    credit3= int(input('Enter credit hours for the class: '))
    if grade3=='a':
        grade3=4.0*credit3
    if grade3=='b':
        grade3=3.0*credit3
    if grade3=='c':
        grade3=2.0*credit3
    if grade3=='d':
        grade3=1.0*credit3
    if grade3=='f':
        grade3=0.0*credit3
            
    grade4=input('\nEnter grade for fourth class: ')
    credit4= int(input('Enter credit hours for the class: '))
    if grade4=='a':
        grade4=4.0*credit4
    if grade4=='b':
        grade4=3.0*credit4
    if grade4=='c':
        grade4=2.0*credit4
    if grade4=='d':
        grade4=1.0*credit4
    if grade4=='f':
        grade4=0.0*credit4
        
    grade5=input('\nEnter grade for fifth class: ')
    credit5= int(input('Enter credit hours for the class: '))
    if grade5=='a':
        grade5=4.0*credit5
    if grade5=='b':
        grade5=3.0*credit5
    if grade5=='c':
        grade5=2.0*credit5
    if grade5=='d':
        grade5=1.0*credit5
    if grade5=='f':
        grade5=0.0*credit5
        
    grade6=input('\nEnter grade for sixth class: ')
    credit6= int(input('Enter credit hours for the class: '))
    if grade6=='a':
        grade6=4.0*credit6
    if grade6=='b':
        grade6=3.0*credit6
    if grade6=='c':
        grade6=2.0*credit6
    if grade6=='d':
        grade6=1.0*credit6
    if grade6=='f':
        grade6=0.0*credit6

    grade7=input('\nEnter grade for seventh class: ')
    credit7= int(input('Enter credit hours for the class: '))
    if grade7=='a':
        grade7=4.0*credit7
    if grade7=='b':
        grade7=3.0*credit7
    if grade7=='c':
        grade7=2.0*credit7
    if grade7=='d':
        grade7=1.0*credit7
    if grade7=='f':
        grade7=0.0*credit7

    grade8=input('\nEnter grade for eighth class: ')
    credit7= int(input('Enter credit hours for the class: '))
    if grade8=='a':
        grade8=4.0*credit8
    if grade8=='b':
        grade8=3.0*credit8
    if grade8=='c':
        grade8=2.0*credit8
    if grade8=='d':
        grade8=1.0*credit8
    if grade8=='f':
        grade8=0.0*credit8
        
    creditTotal= (credit1+credit2+credit3+credit4+credit5+credit6+credit7+credit8)
    gpa= float((grade1+grade2+grade3+grade4+grade5+grade6+grade7+grade8)/creditTotal)

    print ('\n\nYour current GPA is:',gpa)
    
if ask=='7':
    grade1= input('\n\nEnter grade for first class: ')
    credit1= int(input('Enter credit hours for the class: '))
    if grade1=='a':
        grade1=4.0*credit1
    if grade1=='b':
        grade1=3.0*credit1
    if grade1=='c':
        grade1=2.0*credit1
    if grade1=='d':
        grade1=1.0*credit1
    if grade1=='f':
        grade1=0.0*credit1
        
    grade2=input('\nEnter grade for second class: ')
    credit2= int(input('Enter credit hours for the class:'))
    if grade2=='a':
        grade2=4.0*credit2
    if grade2=='b':
        grade2=3.0*credit2
    if grade2=='c':
        grade2=2.0*credit2
    if grade2=='d':
        grade2=1.0*credit2
    if grade2=='f':
        grade2=0.0*credit2
        
    grade3=input('\nEnter grade for third class: ')
    credit3= int(input('Enter credit hours for the class: '))
    if grade3=='a':
        grade3=4.0*credit3
    if grade3=='b':
        grade3=3.0*credit3
    if grade3=='c':
        grade3=2.0*credit3
    if grade3=='d':
        grade3=1.0*credit3
    if grade3=='f':
        grade3=0.0*credit3
            
    grade4=input('\nEnter grade for fourth class: ')
    credit4= int(input('Enter credit hours for the class: '))
    if grade4=='a':
        grade4=4.0*credit4
    if grade4=='b':
        grade4=3.0*credit4
    if grade4=='c':
        grade4=2.0*credit4
    if grade4=='d':
        grade4=1.0*credit4
    if grade4=='f':
        grade4=0.0*credit4
        
    grade5=input('\nEnter grade for fifth class: ')
    credit5= int(input('Enter credit hours for the class: '))
    if grade5=='a':
        grade5=4.0*credit5
    if grade5=='b':
        grade5=3.0*credit5
    if grade5=='c':
        grade5=2.0*credit5
    if grade5=='d':
        grade5=1.0*credit5
    if grade5=='f':
        grade5=0.0*credit5
        
    grade6=input('\nEnter grade for sixth class: ')
    credit6= int(input('Enter credit hours for the class: '))
    if grade6=='a':
        grade6=4.0*credit6
    if grade6=='b':
        grade6=3.0*credit6
    if grade6=='c':
        grade6=2.0*credit6
    if grade6=='d':
        grade6=1.0*credit6
    if grade6=='f':
        grade6=0.0*credit6

    grade7=input('\nEnter grade for seventh class: ')
    credit7= int(input('Enter credit hours for the class: '))
    if grade7=='a':
        grade7=4.0*credit7
    if grade7=='b':
        grade7=3.0*credit7
    if grade7=='c':
        grade7=2.0*credit7
    if grade7=='d':
        grade7=1.0*credit7
    if grade7=='f':
        grade7=0.0*credit7
        
    creditTotal= (credit1+credit2+credit3+credit4+credit5+credit6+credit7)
    gpa= float((grade1+grade2+grade3+grade4+grade5+grade6+grade7)/creditTotal)

    print ('\n\nYour current GPA is:',gpa)
    
if ask=='6':
    grade1= input('\n\nEnter grade for first class: ')
    credit1= int(input('Enter credit hours for the class: '))
    if grade1=='a':
        grade1=4.0*credit1
    if grade1=='b':
        grade1=3.0*credit1
    if grade1=='c':
        grade1=2.0*credit1
    if grade1=='d':
        grade1=1.0*credit1
    if grade1=='f':
        grade1=0.0*credit1
        
    grade2=input('\nEnter grade for second class: ')
    credit2= int(input('Enter credit hours for the class: '))
    if grade2=='a':
        grade2=4.0*credit2
    if grade2=='b':
        grade2=3.0*credit2
    if grade2=='c':
        grade2=2.0*credit2
    if grade2=='d':
        grade2=1.0*credit2
    if grade2=='f':
        grade2=0.0*credit2
        
    grade3=input('\nEnter grade for third class: ')
    credit3= int(input('Enter credit hours for the class: '))
    if grade3=='a':
        grade3=4.0*credit3
    if grade3=='b':
        grade3=3.0*credit3
    if grade3=='c':
        grade3=2.0*credit3
    if grade3=='d':
        grade3=1.0*credit3
    if grade3=='f':
        grade3=0.0*credit3
            
    grade4=input('\nEnter grade for fourth class: ')
    credit4= int(input('Enter credit hours for the class: '))
    if grade4=='a':
        grade4=4.0*credit4
    if grade4=='b':
        grade4=3.0*credit4
    if grade4=='c':
        grade4=2.0*credit4
    if grade4=='d':
        grade4=1.0*credit4
    if grade4=='f':
        grade4=0.0*credit
        
    grade5=input('\nEnter grade for fifth class: ')
    credit5= int(input('Enter credit hours for the class: '))
    if grade5=='a':
        grade5=4.0*credit5
    if grade5=='b':
        grade5=3.0*credit5
    if grade5=='c':
        grade5=2.0*credit5
    if grade5=='d':
        grade5=1.0*credit5
    if grade5=='f':
        grade5=0.0*credit5
        
    grade6=input('\nEnter grade for sixth class: ')
    credit6= int(input('Enter credit hours for the class: '))
    if grade6=='a':
        grade6=4.0*credit6
    if grade6=='b':
        grade6=3.0*credit6
    if grade6=='c':
        grade6=2.0*credit6
    if grade6=='d':
        grade6=1.0*credit6
    if grade6=='f':
        grade6=0.0*credit6
        
    creditTotal= (credit1+credit2+credit3+credit4+credit5+credit6)
    gpa= float((grade1+grade2+grade3+grade4+grade5+grade6)/creditTotal)
    
    print ('\n\nYour current GPA is:',gpa)
    
if ask=='5':
    grade1= input('\n\nEnter grade for first class: ')
    credit1= int(input('Enter credit hours for the class: '))
    if grade1=='a':
        grade1=4.0*credit1
    if grade1=='b':
        grade1=3.0*credit1
    if grade1=='c':
        grade1=2.0*credit1
    if grade1=='d':
        grade1=1.0*credit1
    if grade1=='f':
        grade1=0.0*credit1
    grade2=input('\nEnter grade for second class: ')
    credit2= int(input('Enter credit hours for the class: '))
    if grade2=='a':
        grade2=4.0*credit2
    if grade2=='b':
        grade2=3.0*credit2
    if grade2=='c':
        grade2=2.0*credit2
    if grade2=='d':
        grade2=1.0*credit2
    if grade2=='f':
        grade2=0.0*credit2
    grade3=input('\nEnter grade for third class: ')
    credit3= int(input('Enter credit hours for the class: '))
    if grade3=='a':
        grade3=4.0*credit3
    if grade3=='b':
        grade3=3.0*credit3
    if grade3=='c':
        grade3=2.0*credit3
    if grade3=='d':
        grade3=1.0*credit3
    if grade3=='f':
        grade3=0.0*credit3
    grade4=input('\nEnter grade for fourth class: ')
    credit4= int(input('Enter credit hours for the class: '))
    if grade4=='a':
        grade4=4.0*credit4
    if grade4=='b':
        grade4=3.0*credit4
    if grade4=='c':
        grade4=2.0*credit4
    if grade4=='d':
        grade4=1.0*credit4
    if grade4=='f':
        grade4=0.0*credit4
    grade5=input('\nEnter grade for fifth class: ')
    credit5= int(input('Enter credit hours for the class: '))
    if grade5=='a':
        grade5=4.0*credit5
    if grade5=='b':
        grade5=3.0*credit5
    if grade5=='c':
        grade5=2.0*credit5
    if grade5=='d':
        grade5=1.0*credit5
    if grade5=='f':
        grade5=0.0*credit5
        
    creditTotal= (credit1+credit2+credit3+credit4+credit5)
    gpa= float((grade1+grade2+grade3+grade4+grade5)/creditTotal)

    print ('\n\nYour current GPA is:',gpa)

if ask=='4':
    grade1= input('\n\nEnter grade for first class: ')
    credit1= int(input('Enter credit hours for the class: '))
    if grade1=='a':
        grade1=4.0*credit1
    if grade1=='b':
        grade1=3.0*credit1
    if grade1=='c':
        grade1=2.0*credit1
    if grade1=='d':
        grade1=1.0*credit1
    if grade1=='f':
        grade1=0.0*credit1
    grade2=input('\nEnter grade for second class: ')
    credit2= int(input('Enter credit hours for the class: '))
    if grade2=='a':
        grade2=4.0*credit2
    if grade2=='b':
        grade2=3.0*credit2
    if grade2=='c':
        grade2=2.0*credit2
    if grade2=='d':
        grade2=1.0*credit2
    if grade2=='f':
        grade2=0.0*credit2
    grade3=input('\nEnter grade for third class: ')
    credit3= int(input('Enter credit hours for the class: '))
    if grade3=='a':
        grade3=4.0*credit3
    if grade3=='b':
        grade3=3.0*credit3
    if grade3=='c':
        grade3=2.0*credit3
    if grade3=='d':
        grade3=1.0*credit3
    if grade3=='f':
        grade3=0.0*credit3
    grade4=input('\nEnter grade for fourth class: ')
    credit4= int(input('Enter credit hours for the class: '))
    if grade4=='a':
        grade4=4.0*credit4
    if grade4=='b':
        grade4=3.0*credit4
    if grade4=='c':
        grade4=2.0*credit4
    if grade4=='d':
        grade4=1.0*credit4
    if grade4=='f':
        grade4=0.0*credit4
        
    creditTotal= (credit1+credit2+credit3+credit4)
    gpa= float((grade1+grade2+grade3+grade4)/creditTotal)

    print ('\n\nYour current GPA is:',gpa)
    
if ask=='3':
    grade1= input('\n\nEnter grade for first class: ')
    credit1= int(input('Enter credit hours for the class: '))
    if grade1=='a':
        grade1=4.0*credit1
    if grade1=='b':
        grade1=3.0*credit1
    if grade1=='c':
        grade1=2.0*credit1
    if grade1=='d':
        grade1=1.0*credit1
    if grade1=='f':
        grade1=0.0*credit1
    grade2=input('\nEnter grade for second class: ')
    credit2= int(input('Enter credit hours for the class: '))
    if grade2=='a':
        grade2=4.0*credit2
    if grade2=='b':
        grade2=3.0*credit2
    if grade2=='c':
        grade2=2.0*credit2
    if grade2=='d':
        grade2=1.0*credit2
    if grade2=='f':
        grade2=0.0*credit2
    grade3=input('\nEnter grade for third class: ')
    credit3= int(input('Enter credit hours for the class: '))
    if grade3=='a':
        grade3=4.0*credit3
    if grade3=='b':
        grade3=3.0*credit3
    if grade3=='c':
        grade3=2.0*credit3
    if grade3=='d':
        grade3=1.0*credit3
    if grade3=='f':
        grade3=0.0*credit3

    creditTotal= (credit1+credit2+credit3)
    gpa= float((grade1+grade2+grade3)/creditTotal)

    print ('\n\nYour current GPA is:',gpa)
    
if ask=='2':
    grade1= input('\n\nEnter grade for first class: ')
    credit1= int(input('Enter credit hours for the class: '))
    if grade1=='a':
        grade1=4.0*credit1
    if grade1=='b':
        grade1=3.0*credit1
    if grade1=='c':
        grade1=2.0*credit1
    if grade1=='d':
        grade1=1.0*credit1
    if grade1=='f':
        grade1=0.0*credit1
    grade2=input('\nEnter grade for second class: ')
    credit2= int(input('Enter credit hours for the class: '))
    if grade2=='a':
        grade2=4.0*credit2
    if grade2=='b':
        grade2=3.0*credit2
    if grade2=='c':
        grade2=2.0*credit2
    if grade2=='d':
        grade2=1.0*credit2
    if grade2=='f':
        grade2=0.0*credit2
        
    creditTotal= (credit1+credit2)
    gpa= float((grade1+grade2)/creditTotal)

    print ('\n\nYour current GPA is:',gpa)
    
if ask=='1':
    grade1= input('\n\nEnter grade for first class: ')
    credit1= int(input('Enter credit hours for the class: '))
    if grade1=='a':
        grade1=4.0*credit1
    if grade1=='b':
        grade1=3.0*credit1
    if grade1=='c':
        grade1=2.0*credit1
    if grade1=='d':
        grade1=1.0*credit1
    if grade1=='f':
        grade1=0.0*credit1
        
    creditTotal= (credit1)
    gpa= float((grade1)/creditTotal)
    
    print ('\n\nYour current GPA is: ',gpa)
    
print ('\n\nThank you for using GPA Calculator!')
print (input('Press enter to exit.'))

