standard_tuition= int(input('Enter initial tuition amount: '))
tuition_increase=0.05
tuition_calc=0
q=0
x=0
while x<5:
    if x==0:
        x+=1
        q+=1
        tuition_calc=float((standard_tuition*tuition_increase)+standard_tuition)
        print (str('In ')+str(q)+str(' year, the tuition will be ')+str('$')+str(tuition_calc)+str('.'))
    elif x<4:
        x+=1
        q+=1
        tuition_calc=float((tuition_calc*tuition_increase)+tuition_calc)
        print (str('In ')+str(q)+str(' years, the tuition will be ')+str('$')+str(tuition_calc)+str('.'))
    else:
        x+=1
        q+=1
        tuition_calc=((tuition_calc*tuition_increase)+tuition_calc)
        print (str('In ')+str(q)+str(' years, the tuition will be ')+str('$')+str(tuition_calc)+str('.'))
    
    
