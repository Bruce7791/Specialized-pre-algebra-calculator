import math
from sympy import sieve
from sympy import prime
from sympy.ntheory import isprime
from sympy.ntheory import factorint
from sympy import divisors, divisor_count
from sympy.ntheory import primefactors 
from sympy import lcm
from fractions import gcd


def findPercent(percent, num1):
    a = percent/100
    b = a*num1
    print(percent,"% of", num1, "is", b)

def findPercent2(num1, num2):
    a = num2/num1
    b = a*100
    print(num2,"is", b, "% of", num1)

def findPercent3(num1, num2):
    a = num2-num1
    b = a/num1*100
    if num1 < num2:
        print("The percentage change from", num1, "to", num2, "is a", b, "% increase.")
    elif num1 > num2:
        print("The percentage change from", num1, "to", num2, "is a", b, "% decrease.")
    elif num1 == num2:
        print("There was no percentage increase or decrease.")

def exp(num1, num2):
    product = math.pow(num1, num2)
    print(num1,"raised to the power of",num2,"is",product)

def sqrRoot(sqr):
    print("The square root of", sqr, "is", math.sqrt(sqr))

def fact(num1):
    print("The factorial of your number is:", math.factorial(num1))

def log(num1, num2):
    print("logarithm of",num1, "with base", num2, "=", math.log(num1, num2))

def log10(num1):
    print("Base 10 logarithm of",num1, "=", math.log10(num1))

def logE(num1):
    print("Base E logarithm of",num1, "=", math.log(num1))

def primeRange(numRange1, numRange2):
    print("\nHere are the prime numbers in the range that you entered: ", [i for i in sieve.primerange(numRange1, numRange2)])
    
def primeRange2(numRange):
    sieve.extend(numRange)
    print("\nHere are the prime numbers up to the number you entered: ", sieve._list)
    print("\nThere are", len(sieve._list), "prime numbers up to", numRange)

def primeLocation(numRange):
    print("\nThe prime number at set location", numRange, "is: ", prime(numRange))

def primeOrComposite(num1):
    if isprime(num1) == True:
        print(num1, "is a prime number")
    elif isprime(num1) == False:
        print(num1, "is a composite number")

def primeFactors(num1):
    print("The prime factors that make up", num1, "are", factorint(num1))
    if factorint(num1) == {num1:1}:
        print(num1, "is a prime number")
    else:
        print(num1, "is a composite number")
    
def factorsOfNumbers(num1):
    print("\nHere are the factors of your number: ", divisors(num1))
    print("Your number has", divisor_count(num1), "factors within it")
    if divisor_count(num1) == 2:
        print("Your number is a prime number.")
    else:
        print("Your number is a composite number.")
    print()
    print("The prime factors of your number are", primefactors(num1))
    print("A number’s prime factors are the set of prime numbers (including repeats) that equal that number when multiplied together.")

def gcf1(num1, num2):
    a = gcd(num1, num2)
    print("\nThe greatest common factor of your numbers is", a)

def gcf2(num1, num2, num3, num4):
    a = gcd(num1, num2)
    b = gcd(num3, num4)
    c = gcd(a, b)
    print("\nThe greatest common factor of your numbers is", c)

def leastCM(num1, num2):
    a = lcm(num1, num2)
    print("\nThe least common multiple of your numbers is", a)

def leastCM2(num1, num2, num3):
    a = lcm(num1, num2)
    b = lcm(a, num3)
    print("\nThe least common multiple of your three numbers is", b)

def leastCM3(num1, num2, num3, num4):
    a = lcm(num1, num2)
    b = lcm(num3, num4)
    c = lcm(a,b)
    print("\nThe least common multiple of your four numbers is", c)


while True:
    print("\nWelcome to Bruce's Swiss Army Knife Prealgebra Calculator Version 1.0")
    print("\nThis calculator features 20 operations one will deal with either in basic math or prealgebra")
    print("\nSelect operation.")
    print("1. Calculate the Percentage of a number")
    print("2. Calculate the Percentage of what one number is to another")
    print("3. Calculate Percentage Change")
    print("4. Calculate Exponents")
    print("5. Calculate Square Roots")
    print("6. Calculate Factorials")
    print("7. Calculate Logarithms")
    print("8. Calculate Base 10 Logarithms")
    print("9. Calculate Base E(Euler's Number) Natural Logarithms")
    print("10. Calculate Prime Numbers from a Range of Numbers")
    print("11. Calculate Prime Numbers up to a Certain Number")
    print("12. Calculate the (st/nd/rd/th) Location of a Prime Number")
    print("13. Calculate whether a Number is Prime or Composite")
    print("14. Calculate Prime Factors")
    print("15. Calculate the Factors of a Number, including Prime Factors, and whether the number is a Prime Number or a Composite Number")
    print("16. GCF: Calculate the Greatest Common Factor of Two Numbers")
    print("17. GCF: Calculate the Greatest Common Factor of Three to Four Numbers")
    print("18. LCM: Calculate the Least Common Multiple of Two Numbers")
    print("19. LCM: Calculate the Least Common Multiple of Three Numbers")
    print("20. LCM: Calculate the Least Common Multiple of Four Numbers")
    print()
    choice = input("Enter choice(1/2/3/4/5/6/7/8/9/10/11/12/13/14/15/16/17/18/19/20): ")

    print()
    if choice == '1':
        print("\nFind the percentage of any number.")
        print("\nPlease enter the percentage and the number you want to check.")
        percent = float(input("\nThe percentage: ",))
        num1 = float(input("The number: ",))
        print()
        findPercent(percent, num1)

    elif choice == '2':
        print("\nFind what the percentage of what one number is to another.")
        print("\nPlease enter the two numbers you want to check.")
        num1 = float(input("\nThe larger number: ",))
        num2 = float(input("The smaller number: ",))
        print()
        findPercent2(num1, num2)

    elif choice == '3':
        print("\nCalculate percentage change.")
        print("\nPlease enter the old value and new value to find out the percentage change")
        num1 = float(input("Old value: ",))
        num2 = float(input("New value: ",))
        print()
        findPercent3(num1, num2)

    elif choice == '4':
        print("\nCalculate exponents.")
        num1 = int(input("\nEnter the base number: ", ))
        num2 = int(input("Enter the exponent/power you want your number raised to: ",))
        print()
        exp(num1, num2)

    elif choice == '5':
        print("Calculate square roots.")
        sqr = float(input("\nPlease enter a number to find the square root of it: ", ))
        print()
        sqrRoot(sqr)

    elif choice == '6':
        print("Calculate factorials.")
        num1 = int(input("\nPlease enter the number you want to perform the factorial operation on: ", ))
        print()
        fact(num1)

    elif choice == '7':
        print("Calculate logarithms.")
        num1 = float(input("\nEnter the number you want to get to: ",))
        num2 = int(input("Enter the base number: ",))
        log(num1, num2)

    elif choice == '8':
        print("Calculate base 10 logarithms.")
        num1 = float(input("Enter the number you want to calculate base 10 on: ",))
        log10(num1)

    elif choice == '9':
        print("Calculate base E(Euler's Number) natural logarithms.")
        num1 = float(input("Enter the number you want to calculate base E on: ",))
        logE(num1)

    elif choice == '10':
        print("Calculate Prime Numbers from a Range of Numbers")
        print("\nEnter a range of numbers to get the prime numbers in them")
        numRange1 = int(input("\nPlease enter the first number of your number range: "), )
        numRange2 = int(input("Please enter the second number of your number range: "), )
        primeRange(numRange1, numRange2)

    elif choice == '11':
        print("Calculate Prime Numbers up to a certain number")
        numRange = int(input("\nPlease enter a number to print out the prime numbers up to it: "), )
        primeRange2(numRange)

    elif choice == '12':
        print("Calculate the (st/nd/rd/th) Location of a Prime Number")
        numRange = int(input("\nPlease enter a number to find out which prime number is at that set location in the Prime Number Set: "), )
        primeLocation(numRange)

    elif choice == '13':
        print("Calculate whether a number is prime or composite")
        num1 = int(input("\nPlease enter a number to find out if it is a prime number or a composite number: "), )
        primeOrComposite(num1)

    elif choice == '14':
        print("Calculate prime factors")
        num1 = int(input("\nPlease enter a number to find out the prime factors that make it up: "), )
        primeFactors(num1)

    elif choice == '15':
        print("Calculating the factors of a number, including prime factors, and whether the number is a prime number or a composite number")
        print("\nFactors are the numbers we can multiply together to get another number.")
        num1 = int(input("\nPlease enter your number to find it's factors: ", ))
        factorsOfNumbers(num1)

    elif choice == '16':
        print("GCF: Find the greatest common factor of two numbers")
        print("\nThe greatest common factor (GCF) of a set of numbers is the largest number that’s a factor of all those numbers.")
        num1 = int(input("\nEnter the first number: ",))
        num2 = int(input("Enter the second number: ",))
        gcf1(num1, num2)

    elif choice == '17':
        print("GCF: Find the greatest common factor of three to four numbers")
        print("\nThe greatest common factor (GCF) of a set of numbers is the largest number that’s a factor of all those numbers.")
        print("\n**Enter a zero for your fourth number if there are only three numbers to calculate**")
        num1 = int(input("\nEnter first number: ",))
        num2 = int(input("Enter second number: ",))
        num3 = int(input("Enter third number: ",))
        num4 = int(input("Enter fourth number: ",))
        gcf2(num1, num2, num3, num4)

    elif choice == '18':
        print("LCM: Calculate the least common multiple of two numbers")
        print("\nThe least common multiple (LCM) of a set of numbers is the lowest positive number that’s a multiple of every number in that set.")
        num1 = int(input("\nEnter the first number: ",))
        num2 = int(input("Enter the second number: ",))
        leastCM(num1, num2)

    elif choice == '19':
        print("LCM: Calculate the least common multiple of three numbers")
        print("\nThe least common multiple (LCM) of a set of numbers is the lowest positive number that’s a multiple of every number in that set.")
        num1 = int(input("\nEnter the first number: ",))
        num2 = int(input("Enter the second number: ",))
        num3 = int(input("Enter the third number: ",))
        leastCM2(num1, num2, num3)

    elif choice == '20':
        print("LCM: Calculate the least common multiple of four numbers")
        print("\nThe least common multiple (LCM) of a set of numbers is the lowest positive number that’s a multiple of every number in that set.")
        num1 = int(input("\nEnter the first number: ",))
        num2 = int(input("Enter the second number: ",))
        num3 = int(input("Enter the third number: ",))
        num4 = int(input("Enter the fourth number: ",))
        leastCM3(num1, num2, num3, num4)

    else:
        print("Invalid input")

    while True:
        answer = input('Run again? (y/n): ')
        if answer in ('y', 'n'):
            break
        print('Invalid input.')
    if answer == 'y':
        continue
    else:
        print('Goodbye')
        break
