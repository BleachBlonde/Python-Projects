print ('Speed Converter')
print ('  MPH','\t','KPH')
print ('---------------')
for mph in range (60, 201, 10):
    show1=mph
    kph=mph*0.6214
    floater=float("{0:.1f}".format(kph))
    print (mph, '\t', floater)

input('\nPress ENTER to exit.')
