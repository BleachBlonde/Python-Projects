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
rad1= int(input('Enter Radical to Simplify: '))

print (simpleradicalformat(rad1))
