print("-------Vector Program-------\n\n")

from math import floor
def simpleradical(n):
  nabs = abs(n)
  trial = floor(nabs**0.5)
  coeff = 1
  while trial > 1:
    if n % (trial**2) == 0:
      coeff = trial
      trial = 0
    trial -= 1
  remainder = nabs // coeff**2
  return coeff, remainder

def simpleradicalformat(n):
  if not(isinstance(n, int)):
    return "Input must be an integer"
  elif n == 0 or n == 1:
    return str(n)
  else:
    coeff, remainder = simpleradical(n)
    returnstring = ''
    if coeff > 1:
      returnstring = str(coeff)
    if n < 0:
      returnstring += "i"     
    if remainder > 1:
      returnstring += '√' + str(remainder)
  return returnstring

print("Enter coeffecients for u vector _i+_j+_k\n")
u1= int(input("i coeffecient is: "))
u2= int(input("j coeffecient is: "))
u3= int(input("k coeffecient is: "))
print("\nEnter coeffecients for v vector _i+_j+_k\n")

v1= int(input("i coeffecient is: "))
v2= int(input("j coeffecient is: "))
v3= int(input("k coeffecient is: "))

crossI= ((u2*v3)-(u3*v2))
crossJ= ((u1*v3)-(u3*v1))
crossK= ((u1*v2)-(u2*v1))
print("\nThe result is",crossI,"i -",crossJ,"j +",crossK,"k","\n")

dotPro= ((u1*v1)+(u2*v2)+(u3*v3))
print("When u is dotted with v the result is:", dotPro,)

magnitudeU= (u1**2+u2**2+u3**2)
magnitudeUSim= simpleradicalformat(magnitudeU)
print("The magnitude of u is:",magnitudeUSim)

magnitudeV= (v1**2+v2**2+v3**2)
magnitudeVSim= simpleradicalformat(magnitudeV)
print("The magnitude of v is:",magnitudeVSim)

magnitudeUxV= (crossI**2+crossJ**2+crossK**2)
crossSim= simpleradicalformat(magnitudeUxV)
print("The magnitude of U crossed with V is:",crossSim,"\n")

input("Press any key to exit.")
