#Import libraries
import random

#List of characters to be used in the password
password =['0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0']
letters=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z',]
numbers =['1','2','3','4','5','6','7','8','9','9']
symbols = ['!','@','#','$','%','^','&','*','(',')','-','_','=','+','[',']','{','}','|',';',':','"',',','<','.','>','/','?','`','~','\\']
#Code to generate a random password
pw = ['0','0','0','0','0','0','0','0','0','0','0']
for i in range(1,11):
  chartype = random.randint(1,3)
  if chartype == 1:
    pw[i] = random.choice(letters)
  elif chartype == 2:
    pw[i] = random.choice(numbers)
  else:
    pw[i] = random.choice(symbols)
pwS = ''.join(pw)
print(pwS)