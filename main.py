## --> PROBLEMA #1 <--
# 1. Calcular el salario neto de un trabajador. 
# Es necesario conocer horas trabajadas, 
# pago por hora al trabajador y descuentos fijos al trabajo bruto con impuesto (12% del salario bruto). 
# 120 Horas trabajadas a razón de 13.45 por hora.

horas_trabajadas = int(input("Cuantas horas trabajaste: "))
pago_por_hora = float(input("Cuanto es tu pago por hora: "))
salario = pago_por_hora * horas_trabajadas
descuento_fijo = 0.12 * salario
salario_neto = salario - descuento_fijo
print("Tu salario neto es", salario_neto)

## --> PROBLEMA #2 <--
# 2. Suma de todos los números pares. La suma se realizará usando todos los números entre el 2 y el 100.
suma = 0
for i in range(0,102,2):
    suma += i
print("La suma de todos los numeros pares entre 2 y 100 es:", suma)

## --> PROBLEMA #3 <--
# 3. Desplegar (imprimir) la lista de números del 1 al 100 cuyo valor termine 6. 
value = "6"
for i in range(1,101):
    if (str(i).endswith("6")):
        print(i)
    
## --> PROBLEMA #4 <--
# 4. Calcular la suma de los números del 1 al 1000.

suma = 0
for i in range(1,1001):
    suma += i
print("La suma de todos los numeros de 1 al 1000 es:", suma)

## --> PROBLEMA #5 <--
# Calcular la media de las estaturas de las siguientes personas:
# 1     66 
# 2     69 
# 3     71 
# 4     70 
# 5     75 
# 6     67 
# 7     69 
# 8     64 
# 9     73 
# 10    71
# Mencione cuantas de esas personas son más altas que la media de la estatura y cuantas son más bajas.
personas = 1
suma = 0
personasMayorQueMedia = 0
personasMenorQueMedia = 0
estaturas = []

while (personas <= 10):
    estatura = int(input("Entra la estatura en pulgadas: "))
    estaturas.append(estatura)
    suma += estatura
    personas += 1

print("La suma de las estaturas es", suma)
media = suma/10
print("La media de las estaturas de las personas es: %.2f" % (media))
for i in range(0,len(estaturas)):
    if estaturas[i] > media:
        personasMayorQueMedia += 1
    elif estaturas[i] < media:
        personasMenorQueMedia += 1
print("Hay",personasMayorQueMedia,"personas mas altas que la media.\n"+"Hay",personasMenorQueMedia,"personas mas bajas que la media.")

## --> PROBLEMA #6 <--

# Realizar un programa en donde, cuando el usuario entre un numero entre 1 y 7 el programa
# arroje un mensaje que indique s que dia corresponde ese numero ingresado, ademas, 
# si el usuario entra un numero que no esta entre 1 y 7 el programa debe pedir que 
# se entre otro numero entre eses rango y al entrar el numero 9 el programa se cierre.

opcionusuario = 0

while (opcionusuario != 9):
    
    opcionusuario = int(input("Escribe un numero para saber a que dia de la semana corresponde (Si desea cerrar el programa persione 9): "))

    if opcionusuario == 1:
        print("Lunes\n")
    
    elif opcionusuario == 2:
        print("Martes\n")

    elif opcionusuario == 3:
        print("Miercoles\n")
    
    elif opcionusuario == 4:
        print("Jueves\n")

    elif opcionusuario == 5:
        print("Viernes\n")

    elif opcionusuario == 6:
        print("Sabado\n")

    elif opcionusuario == 7:
        print("Domingo\n")
    
    elif opcionusuario != 9:
        print("\nEntra un numero entre 1 y 7.")
 
## ---> QUESTION 6 <---

food_charge = input("Enter the charge for the food: ")

food_charge = float(food_charge)

# 20% tip
tip = 0.20 * food_charge

# 8% sales tax
sales_tax = 0.08 * food_charge

total_owed = food_charge + tip + sales_tax

print("The tip owed is $"+str(format(tip,",.2f"))+".\n"+"The sales tax owed is $"+str(format(sales_tax,",.2f"))+".\n"+"The total amount owed is $"+str(format(total_owed,",.2f"))+".")

## --> QUESTION 7 <--
number = input ("enter a number between 1 and 100: ")

try:
    number = int(number)
    if number < 1 or number > 100: 
        print("error invalid number")

    elif number % 2 == 0:
        print("number is even")

    elif number % 2 != 0:
        print("number is odd")

except ValueError:
    print("error enter a number")
    
## --> QUESTION 8 <--

first_color, second_color = input("enter the names of two primary colors to mix: ").split()

if first_color == second_color:
    print("enter two different primary colors")

elif first_color == "red" or second_color == "red":
    if first_color == "blue" or second_color == "blue":
        print("you get purple")
    elif first_color == "yellow" or second_color == "yellow":
        print("you get orange")

elif first_color == "blue" or second_color == "blue":
    if first_color == "yellow" or second_color == "yellow":
        print("you get green")

else:
    print("invalid color entry")

    
## --> QUESTION 9 <--

# Write a while loop that lets the user enter a number. 
# The number should be multiplied by 10, 
# and the result assigned to a variable named product. 
# The loop should iterate as long as the product is less than 100.

product = 0
while (product < 100):
    num = int(input("Enter a number: "))
    product = num * 10

## --> QUESTION 10 <--

# Write a for loop that displays the following set of numbers:
# 0, 10, 20, 30, 40, 50 . . . 100

for i in range (11):
    print(i*10)

## --> QUESTION 11 <--

# Write a loop that asks the user to enter a number. 
# The loop should iterate 10 times and keep a running total of the numbers entered.

sum = 0
for i in range(10):
    sum += int(input("Enter a number: "))
    print("The sum is: ",sum)

## --> QUESTION 12 <--

# Write a program that prints numbers starting at 20 and ending at 0. 
# For every odd number, print "Buzz" instead of the number, and for every even number, 
# print "Fizz" instead of the number.

count = 20
while count >= 0:
    if count % 2 == 0:
        print("Fizz")
        count -= 1
    else:
        print("Buzz")
        count -= 1
        
   ## --> QUESTION 13 <--

# Write a program with a loop that asks the user to enter a series of positive numbers. 
# The user should enter a negative number to signal the end of the series. 
# After all the positive numbers have been entered, the program should display the sum.

nums = 0
sum = 0
while not nums < 0:
    sum += nums
    if nums >= 0:
        nums = int(input("Enter a positive number (or negative to QUIT): "))
    else:
        break
print("The total sum is", sum)
    

## --> QUESTION 14 <--

# At one college, the tuition for a full-time student is $8,000 per semester. 
# It has been announced that the tuition will increase by 3 percent each year for the next 5 years. 
# Write a program with a loop that displays the projected semester tuition for the next 5 years.

tuition = 8000
rate_of_increase = 0.03

for i in range(5):
    new_tuition = (tuition * rate_of_increase) + tuition
    tuition += tuition * rate_of_increase
    format_tuition = "{:.2f}".format(tuition)
    print("year:", i+1 ,"tuition:" , format_tuition)


## --> QUESTION 15 <--

# Write a program that uses a nested loops to draw this pattern:

# *******

# ******

# *****

# ****

# ***

# **

# *

design = "*******"
loop = True
while loop:
    if "*" in design:
        print(design)
        design = design.replace("*","",1)    
    else:
        loop = False

## --> QUESTION 16 <--

# Write a program that prints out all numbers from list_a: [0,1,2,3,4,5] 
# that do not have a corresponding number in another list_b: [1,3,5,7,9]. 
# When a number in list_a is determined to not have a duplicate in list_b, 
# print out "{num} is not in list_b".

# For example: "0 is not in list_b"

list_a = [0,1,2,3,4,5]
list_b = [1,3,5,7,9]

for i in range(len(list_a)):
    if list_a[i] not in list_b:
        print(list_a[i] , "is not in list_b")
        
## --> QUESTION 17 <--

# Write a function named times_ten. The function should accept an argument and display the product of its argument multiplied by 10.

def times_ten(num):
    print(num * 10)


## --> QUESTION 18 <--

# Write a program that asks a user to enter a distance in kilometers, then converts that distance to miles and prints it out. The conversion formula is as follows:

# Miles = Kilometers x 0.6214

def distanceToMiles(km):
    return km * 0.6214

kilometers = float(input("Enter a distance in kilometers: "))
miles = distanceToMiles(kilometers)
print("The distance in miles is:", "{:.4f}".format(miles))
    

## --> QUESTION 19 <--

# Write a function count_up that prints out a number up to and including the passed in parameter number.

def count_up(num):
    count = 0
    if count <= num:
        for i in range (0, num+1):
            print(i)


## --> QUESTION 20 <--

# Write a program that keeps track of running piggybank deposits. 
# The program should receive input from a user that will enter the amount to deposit into the piggybank. 
# Use a function, add, which takes an argument number from the user input and adds it to a global sum variable. 
# After the 5th deposit, print out the running total thus far.

def add(num):
    global sum
    return sum + num

sum = 0
count = 0
while sum >= 0:

    if sum >= 0:
        deposit_amount = float(input("Amount to deposit: "))
        sum = add(deposit_amount)
        count += 1

        if count % 5 == 0:
            print("Running total thus far: $" + "{:.2f}".format(sum))
    
   ## --> QUESTION 21 <--

# Write a program that counts all the vowels in a string. 
# The program should allow a user to enter a string input and print out a number response.

def count_vowels(string):
    vowels = ""
    string = string.lower()

    for char in string:
        if char in "aeiou":
            vowels += char
    
    return len(vowels)

user_input = input("Enter a sentence (string): ")

numOfVowels = count_vowels(user_input)

print(numOfVowels)


## --> QUESTION 22 <--

# Write a function that accepts two string arguments: str and substr. 
# The function should count the number of times the substr is in str and return that number.

def count(str, substr):
    numOfSubstr = 0
    while substr in str:
        
        if substr in str:
            str = str.replace(substr, "", 1)
            numOfSubstr += 1

    return numOfSubstr

## --> QUESTION 23 <--

# Given this string: "Hello, my name is Joe. I love long walks in the park and staring at stars at night."

# Write a program that prints out the following:

# The number of upper case letters in the string
# The number of lower case letters in the string
# The number of whitespace characters in the string

def upper_case(string):
    numOfUpper = 0
    for char in string:
        if char.isupper():
            numOfUpper += 1
    return numOfUpper

def lower_case(string):           
    numOfLower = 0
    for char in string:
        if char.islower():
            numOfLower += 1
    return numOfLower

def whitespace(string):
    numOfWhitespace = len(string) - len(string.replace(" ",""))
    return numOfWhitespace 
        
string = "Hello, my name is Joe. I love long walks in the park and staring at stars at night."
result_upper = upper_case(string)
result_lower = lower_case(string)
result_whitespace = whitespace(string)

print("number of upper case letters:" , result_upper , "\nnumber of lower case letters:" , result_lower, "\nnumber of whitespace:" , result_whitespace)


## --> QUESTION 24 <--

# Write a program that asks the user to enter a series of single-digit numbers with nothing separating them. 
# The program should display the sum of all the single-digit numbers in the string. 
# For example, if the user enters 1234, the method should return 10, which is the sum of 1, 2, 3, and 4.

def sumOfNums(numbers):
    sum = 0
    for digit in numbers:
        sum += int(digit)
    return sum

user_input = input("Enter a series of single-digit numbers with nothing seperating them: ")

result = sumOfNums(user_input)
print(result)


## --> QUESTION 25 <--

# Design a program that generates an 8-digit passcode consisting of random numbers. 
# The program should generate eight random numbers, each in the range of 0-9, and assign each number to a list. 
# Note: random numbers were discussed in Chapter 5. 
# Then write another loop that displays the contents of the list.
import random
def passcode():
    passcode = []
    while len(passcode) <= 8:
        digits = random.randrange(10)
        passcode.append(digits)
    return passcode

loop = True
while (loop):
    user_input = input("Do you want to generate a passcode? (y/n): ")
    if user_input == "y":
        print(passcode())
    elif user_input == "n":
        loop = False
        break


# --> QUESTION 26 <--

# A positive integer greater than 1 is said to be prime if it has no divisors other than 1 and itself. 
# A positive integer greater than 1 is composite if it is not prime. 
# Write a program that asks the user to enter an integer greater than 1, 
# then displays all of the prime numbers that are less than or equal to the number entered. 

# The program should meet the following criteria:
def isPrime(number):
    if number == 2 or number == 3:
        return "is prime"
    elif number % 3 != 0 and number % 2 != 0:
        return "is prime"
    else:
        return "not prime"

# Once the user has entered a number, the program should populate a list with all of the integers from 2 up through the value entered.
user_input = int(input("Enter an integer greater than 1: "))
list = []
for i in range(2,user_input+1):
        list.append(i) 

# The program should then use a loop to step through the list. 
loop = True
while (loop):

# The loop should pass each element to a function that displays the element whether it is a prime number
    for number in list:
        print(number,isPrime(number))
    
        if number == user_input:
            loop = False
            break


## --> QUESTION 27 <--

# Given the following list and nested lists:

scores = [['Jack', 'Josh', 'Joe'],[90, 88, 56],[67, 88, 87],[88, 99, 78]]

# Write a program that turns this into an ASCII art table with the scores in their correct places. 
# You may design the table however you like. 
# The nested lists are the rows and the indexes of the nested lists are the columns. 
# In the end, you should have a table with 4 rows (first one being the student names) and 3 columns (one for each student).

row_names = scores[0][0] + " | " + scores[0][1] + " | " + scores[0][2]
print ("-" * len(row_names))
print(row_names)
for i in range (1,4):
    print ("-" * len(row_names))
    print(" " + str(scores[i][0]) + " " + " | " + " " + str(scores[i][1]) + " " + " | " + str(scores[i][2]))
print ("-" * len(row_names))

#  --> QUESTION 28 <--
# A grocery store has a reward system that gives customers redeemable points based on the amount spent on groceries. 
# The points are awarded as follows:
# If a customer spends <= $50, they are awarded 1 point for each dollar spent.
# If a customer spends > $50 and < $150, they are awarded 2 points for each dollar spent
# If a customer spends >= $150, they are awarded 3 points for each dollar spent.
# You can assume all grocery items are priced to the dollar with tax included (no cents). 

# Write a program that asks a customer to enter the total dollar amount spent for the trip, 
# then displays the number of points awarded.

total_spent = int(input("Enter the total dollar amount spent for the trip: "))
if total_spent <= 50:
    points = 1
    total_spent *= points

elif total_spent > 50 and total_spent < 150:
    points = 2
    total_spent *= points

elif total_spent >= 150:
    points = 3
    total_spent *= points

print("The number of points awarded are:",total_spent)


# --> QUESTION 29 <-- 

# define an input that accepts an age (number)
age = int(input("Enter an age (number): "))

# check if age is at most 1
if age <= 1:
    print("infant")

# check if age older than 1 but at most 13
elif age > 1 and age <= 13:
    print("child")    

# check if age is older than 13 but at most 20
elif age > 13 and age <= 20:
    print("teenager")

# otherwise print "adult"
else:
    print("adult")


# --> QUESTION 30 <--

# Write a while loop that lets a user enter a number less than 10. 
# If the number inputted exceeds 10, print an error and ask for the number again, 
# in which a user may enter the same or a different number. 
# The number should be incremented by 5, and the result assigned to a variable named sum. 
# The loop should continue to iterate as long as the sum is less than 50. When sum exceeds 30, 
# it should print "Almost there..." until it reaches or exceeds 50. 
# Once it does, print out "your final sum is {replace with final sum}". 

# For example, if the sum is currently 45 and the user inputs 4, 
# the program will not enter the loop again since the new sum will be 54 and should then print "your final sum is 45".

sum = 0
num = int(input("Enter number less than 10: "))

while sum < 50:
    
    if num > 10:
        print("Invalid. Number greater than 10.")
        num = int(input("Enter number less than 10: "))

    num += 5
    sum += num

    if sum > 30 and sum < 50:
        print("Almost there...")

print("your final sum is", sum)


# --> QUESTION 31 <--
# The flowchart shows a program's steps to troubleshooting a lamp issue. 
# Turn the following diagram into a program where the program will first prompt the user with "What is wrong?". 
# If the user enters "Lamp doesn't work", 
# then the program should proceed to ask the questions depicted in the diagram and print out the responses accordingly. 

# If any other issue is inputted initially by the user, ignore and repeat the same initial question until the correct issue is presented by the user.

troubleshoot = input("What is wrong? ")

while troubleshoot.lower() != "lamp doesn't work":
    troubleshoot = input("What is wrong? ")

if troubleshoot.lower() == "lamp doesn't work":
    response = input("Lamp plugged in? ")  
    if response.lower() == "no":
        print("Plug in lamp")
    elif response.lower() == "yes":
        response = input("Bulb burned out? ")
        if response.lower() == "yes":
            print("Replace Bulb")
        elif response.lower() == "no":
            print("Get a new lamp")



# # --> QUESTION 32 <--
# Unfortunately, your landlord has announced that they will be increasing rent annually by 2% starting next year. 
# Write a program that takes a user's current monthly rent amount (integer) and the number of years (integer), 
# starting the following year, the user plans to stay at the apartment, 
# and calculates how much they will spent total in that duration of stay. 
# The program should print this amount back to the user.

current_rent = int(input("What is your current monthly rent amount? "))
years = int(input("How many years do you plan to stay at the apartment? "))
rate_of_increase = 0.02
total = 0

for i in range(years): 
    new_rent = (current_rent * rate_of_increase) + current_rent
    current_rent = new_rent
    total += current_rent

format_total = "{:.2f}".format(total*12)  
print("You will spend a total of $" + str(format_total) + " in " + str(years) + " years.")
   
# # --> QUESTION 33 <--
# # Write a function piglatinize that accepts a sentence as an argument, 
# # uses that parameter value, and replaces words in the sentence that consist of at least 4 letters into their Pig Latin counterpart 
# # and then displays the converted sentence. 
# # In this version, to convert a word to Pig Latin, you remove the first letter and place that letter at the end of the word. 
# # Then, you append the string "ay" to the word. For example:

# # piglatinize('I want a doggy')
# # // >>> I antway a oggyday


def piglatinize(sentence):

    sentence = sentence.split()

    final_sentence = []

    for word in sentence:
        
        if len(word) >= 4:
        
            substring = word[1:]
                
            new_word = substring + word[0] + "ay"
        
            final_sentence.append(new_word)
        
        else:
            final_sentence.append(word)
        

    return (" ".join(final_sentence))

## sample of output

print(piglatinize('I want a doggy'))


# --> QUESTION 34 <--
# Write a program that reads the contents of a text file. 
# Feel free to create your own with at least three lines of words. 
# The program should create a dictionary in which the key-value pairs are described as follows:

# The keys are the individual words in the file.
# The values are the line numbers in the file where the word (the key) is found.

# For example, suppose the word "hello" is found in lines 1, 2, 3, and 4. 
# The dictionary would contain an element in which the key was the string "hello" and the value was a list of the line numbers [1,2,3,4].

# Once the dictionary is built, the program, in an infinite while loop, should prompt the user for a word. 
# When the user enters the word, the program should display what line numbers the word can be found on. 
# If the word is not found in the dictionary, the program should display: "{replace with user-inputted word} does not exist in the file".

## sample program with own txt file
output = open('sample.txt', 'w')
output.write('Jeanelle is a student\n')
output.write('The college is in California\n')
output.write('Happy holidays to everyone and a happy new year\n')     
output.close()

new_file = open('sample.txt', 'r')

my_dict = {}
loop = 0

for line in new_file:
    loop += 1
    line_num = loop
    for word in line.split():
        word = word.lower()

        if word not in my_dict:
            my_dict[word] = line_num
        
        elif word in my_dict and my_dict[word] == line_num:
            break

        else:
            my_dict[word] = [my_dict[word],line_num]

infinite_loop = True
while (infinite_loop):
    user_input = input ("Enter a word to find it's location: ")

    if user_input.lower() in my_dict:
        user_input = user_input.lower()
        print("The word is found in line" , my_dict[user_input])
    
    else:
        print(user_input + " does not exist in the file")
