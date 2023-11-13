# excercise 1 
def prod3(a,b,c):
  return a*b*c

print("excerise 1")
print(prod3(4, 2, 10))

# excercise 2
def quadProd3(d,e,f):
  return (d**2)*(e**2)*(f**2)

print("excercise 2")
print(quadProd3(1,2,3))

# excercise 3
def bmi(weight, height):
    return weight/(height**2)

print("excercise 3")
print(bmi(80, 1.8))

#excercise 4
def CG(bmi,age,gender):
    return 1.294*bmi+0.2*age-11.4*gender-0.8

print("excercise 4")
print(CG(24.69135588,43,0))

#excercise 5
def dividend(rest,quotient,divisor):
    return quotient*divisor+rest

print("excercise 5")
print(dividend(1,3,3))

#excercise 6
def compareLengths(string1,string2):
    if len(string1)==len(string2):
        return True
    else:
        return False

print("excercise 6")
print(compareLengths("PSV Eindhoven", "FC Utrecht"))

# excercise 7
def sumDigits(threedigits):
    first = threedigits // 100
    second = (threedigits % 100)//10
    third = threedigits % 10
    
    return first + second + third
print("excercise 7")
print(sumDigits(975))

#excercise 8
def sumManyDigits(alotdigits):
   
    part1 = int(str(alotdigits)[0:3])
    part2 = int(str(alotdigits)[3:6])
    part3 = int(str(alotdigits)[6:9])
    return sumDigits(part1) + sumDigits(part2) + sumDigits(part3)

    # other option
    #part11 = alotdigits // 1000000
    #part22 = (alotdigits % 1000000) // 1000
    #part33 = alotdigits % 1000
    #return sumDigits(part11) + sumDigits(part22) + sumDigits(part33)

print("excercise 8")
print(sumManyDigits(123456789))

# excercise 10
# excercise 18
# excercise 20
# excercise 21



# excercise 26
def isPrime(num):
    i =2
    prime = True
    target = num//2
    while i < target and prime:
        if num % i == 0:
            prime = False
        i = i + 1
    return prime
print(isPrime(45))

# excercise 28


