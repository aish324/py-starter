person="aishwarya"
percentage = 97
print("hello")
print("I am Aishwarya")

word = "this is a string . \nwe are creating it in python."
print(word)

word = "this is a string . \t we are creating it in python."
print(word)

word = "this is a string .   we are creating it in python."
print(word)

print(f"hello my name is {person} and  my percentage is {percentage}%")

print(person  +   word)

print(type(person))
print(type(percentage))

name = input("Enter Your Name : ")
city = input("Enter Your City : ")
percentage = float(input("Enter Your Percentage : "))
age = int(input("Enter Your Age : "))

print(f"hello my name is {name} i am from {city} my percentage is {percentage}% and i am {age} year old")

a = 10
b = 20

a,b=b,a

print("value of a , b = " ,a,b)

a = 100
b = 200
temp = a
a = b
b = temp
print("value of a , b = " ,a,b)

a = 45
b = 10

print("Addition is ",a+b)
print("substraction is ",a-b)
print("multiplication is ",a*b)
print("division is ",a/b)
print("floor division is ",a//b)
print("exponentiation is ",a**4)

# # Write a Python program to enter length and breadth of a rectangle and find its Area

L = 6
b = 5
print("the area of rectangle is ", L*b)

# # Write a Python program to enter base and height of a triangle and find its area..
B = 12
H = 16
print("the area of triangle is ",0.5*B*H)

# # 5. Write a python Program to calculate Square of given number
num = int(input("enter a number :"))
print(f"the square of {num} is : ",num**2)

# # 6. Write a python Program to calculate cube of given number
num = int(input("enter a number :"))
print(f"the square of {num} is : ",num**3)

# # 7. Write a Python program to enter marks of five subjects and calculate total, and percentage.
m1 = int(input("enter the marks m1:"))
m2 = int(input("enter the marks m2:"))
m3 = int(input("enter the marks m3:"))
m4 = int(input("enter the marks m4:"))
m5 = int(input("enter the marks m5:"))
total = (m1+m2+m3+m4+m5)
percentage = (total/5)
print("the total marks are :",total)
print("the percentage is :",percentage)

# # 8. Write a Python program to enter P, T, R and calculate Simple Interest.
p = int(input("enter the value of p:"))
t = int(input("enter the value of t:"))
r = int(input("enter the value of r:"))
print("the simple interest is ",(p*t*r)/100)

# # 9. Write a Python program to enter length and breadth of a rectangle and find its perimeter.
l = int(input("enter the lenght l:"))
w = int(input("enter the width w:"))
print("the perimeter is ",(l+w)*21)

#WAP to accept a number & print it is even or odd number
n = int(input("enter a number n:"))
if n % 2 == 0:
    print("even number")
else:
    print("odd")

# WAP to check entered number is divisible by 5 or not
num = int(input("enter the number :"))
if num%5 == 0:
    print("divisible by 5")
else:
    print("not divisible")
    
''' Accept the bike price from user & add road tax as follows
 
      Price > 80000   15 % TAX
      Price > 40000 & <80000  10% TAX
      Else                       5% TAX'''

price = int(input("enter the price :"))
if price  > 80000:
    print("the tax is 15% ")
elif price>40000 and price<80000:
    print("the tax is 10%")
else:
    print("the tax is 5%")
    
price = int(input("enter the price :"))
if price  > 80000:
    tax = price*0.15
elif price>40000 and price<80000:
    tax = price*0.1
else:
    tax = price*0.5
print("the tax is",tax)
print("the total price is ",price+tax)
    
# Write a program that displays the day of the week corresponding to the number entered. i.e., 
#1 - "Monday", 2- "Tuesday" and so on. 
num = int(input("enter the number :"))
if num == 1:
    print("monday")
elif num == 2:
    print("tuesday")
elif num == 3:
    print("wednesday")
elif num == 4:
    print("thursday")
elif num == 5:
    print("friday")
elif num == 6:
    print("saturday")
elif num == 7:
    print("sunday")
else:
    print("no week day")
    
#Write a Python program to input electricity consumption unit and 
#calculate totalel ectricity bill according to the given condition:
# For first 50 units Rs. 0.50/unit For next 100 units Rs. 0.75/unit For 
#next 100 units Rs. 1.20/unit For unit above 250 Rs. 1.50/unit An
# additional surcharge of 20% is added to the bill 
unit = int(input("enter the total units :"))
if unit <= 50 :
    bill = unit*0.5 
elif unit>50 and unit<=150 :
    bill = 50*0.5 + (unit-50)*0.75
elif unit>150 and unit<=250:
    bill = 50*0.5 + 100*0.75 + (unit-150)*1.20
else:
    bill = (50*0.5 + 100*0.75 + 100*1.20 + (unit-250)*1.50)
add = bill*0.2 

print("the total bill is :",bill+add)


 
'''1Add
2Sub
3Mul
4Div
5Floor div
6Exponentiation 
Ask user to select the number & based on that calculate the operation'''
n1 = int(input("enter first number n1:"))
n2 = int(input("enter the second number n2:"))
print("selsct an option")
print("1.Add \n 2.Sub \n 3.Mul \n 4.Div \n 5.Floor division \n 6.Exponential")
opt = int(input("select an option opt:"))
if opt == 1:
    print(n1+n2)
elif opt == 2:
    print(n1-n2)
elif opt == 3:
    print(n1*n2)
elif opt == 4:
    print(n1/n2)
elif opt == 5:
    print(n1//n2)
else:
    print(n1**n2)

n1 = int(input("enter first number n1:"))
n2 = int(input("enter the second number n2:"))
print("selsct an option")
print("\nSelect an option:")
print("1. Add")
print("2. Subtract")
print("3. Multiply")
print("4. Divide")
print("5. Floor Division")
print("6. Exponential")

option = int(input("select an option fro above :"))
match option:
    case 1:
        print("the output is :",n1+n2)
    case 2:
        print("the output is :",n1-n2)
    case 3:
        print("the output is :",n1*n2)
    case 4:
        print("the output is :",n1/n2)
    case 5:
        print("the output is :",n1//n2)
    case 6:
        print("the output is :",n1**n2)
    case default:
        print("you have not selected any of the above options")
    
#Accept a number from user & check number is Armstrong number or not

num = int(input("Enter a number: "))
original = num
result = 0
n = len(str(num))  

while num > 0:
    digit = num % 10
    result += digit ** n
    num = num // 10

if result == original:
    print(original, "is an Armstrong number.")
else:
    print(original, "is NOT an Armstrong number.")


# WAP to print even numbers from 121 to 229 using a for loop.
i = 121 
for i in range (121,230):
    if(i % 2 == 0):
      print(i)
      i += 1
    

#  WAP to print odd numbers from 521 to 229 using a while loop.
i = 521
while (i<=521 and i>=229 ):
    if(i % 2 != 0):
     print(i)
    i += 1
#  Write a Python program to print all alphabets from a to z  using  for loop
i = abs("a")
for i in range("a","z"):
    print(i)

#  Write a Python program to find the sum of all even numbers between 1 to n.
n = int(input("enter a number :"))
i = 1 
r = 0 
for i in range (1,n):
    if i % 2 == 0:
        r = r+i
    print(r)
    
      #or
      
n = int(input("enter a number :"))
i = 1 
r = 0 
while i<=n:
    if i % 2 == 0:
        r = r+i
    i +=1
    print(r)
    
#  Write a Python program to find the sum of all odd numbers between 1 to n.
n = int(input("enter a number :"))
i = 1 
r = 0 
for i in range (1,n):
    if i % 2 != 0:
        r = r+i
    print(r)
    
    #or

n = int(input("enter a number :"))
i = 1 
r = 0 
while i<=n:
    if i % 2 != 0:
        r = r+i
    i +=1
    print(r)
    
#  Write a Python program to count number of digits in any number
num = int(input("enter a number :"))
n = len(str(num))
print(n)

# WAP to print table of given no
n = int(input("enter a number :"))
i = 0 
for i in range (1,11):
    print(f"{n} x i :",n*i)
    
    
# WAP to print squares from 1 to20
i = 0 
for i in range (1,21):
    print(f"{i} x {i} :", i*i)


# for loop
i=1

while i<=12:
    if i==5:
        break
    print(i)
    i+=1


i=0

while i<=10:
    i+=1
    if i==5:
        continue
    print(i)


for a in range(50,5,-3):
     print(a)
     
     
row = 1 
while row<=3 :
    col=1 
    while col<=5:
        print("* ",end="")
        col += 1
    print("")
    row +=1
    
row = 1 
while row<=5 :
    col = 1 
    while col<=row:
        print("* ",end="")
        col+=1
    print("")
    row+=1
    
# dry run
'''row = 1 row<=5 col=1 
row col       
 
1	1	        1<=1              *
2	1 2	        1<=2,2<=2             * *
3	1 2 3	    1<=3,2<=3,3<=3             * * *
4	1 2 3 4	    1<             * * * *
5	1 2 3 4 5	              * * * * *

row = 1
while row <=5:
    col = 1
    while col<=row:
        print(f"{col}",end="")
        col +=1
    print("")
    row+=1

row = 5
while row >=1 :
    col = 1
    while col<=row:
        print(" * ",end="")
        col *=1
    print("")
    row+=1'

 #create 4 functions add,sub, mul, div'''

#Pass value as argument & calculate & display the result ( return )

def add(a, b):
    return a + b

def sub(a, b):
    return a - b

def mul(a, b):
    return a * b

def div(a, b):
    if b != 0:
        return a / b
    else:
        return "Cannot divide by zero"

num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

print("Addition:", add(num1, num2))
print("Subtraction:", sub(num1, num2))
print("Multiplication:", mul(num1, num2))
print("Division:", div(num1, num2))




# Write a program to create a function that takes two arguments, name and age, and print their value.
def info(name,age):
    print("Name",name)
    print("Age",age)
info("Aishwarya",23)
# Write a program to create function calculation() such that it can accept two variables and calculate 
# and subtraction. Also, it must return both addition and subtraction in a single return call
def calculation(a,b):
    add = a+b
    sub = a-b
    return add,sub
add_result , sub_result = calculation(10,5)
print("Addition",add_result)
print("Substraction",sub_result)
# Write a program to create a function show_employee() using the following conditions.
# ●  	It should accept the employee’s name and salary and display both.
# ●  	If the salary is missing in the function call then assign default value 9000 to salary
def show_employee(name,salary=9000):
    print("Name:",name)
    print("Salary:",salary)
show_employee("Rahul")
show_employee("Shree",12000)
# 4.	Accept a number from the user, create a function isPrime(), which accepts a number from a parameter & 
#check prime or not. If number is prime return True & number else return false & number
def is_prime(num):
    if num <= 1:
        return False
    for i in range(2,num):
        if num % i == 0:
            return False
        else:
            return True
is_prime(5)

        
# 5.	Create menu driven calculation (add,sub,multiply, divide, mod) using function
def add(a, b):
    return a + b

def sub(a, b):
    return a - b

def mul(a, b):
    return a * b

def div(a, b):
    if b != 0:
        return a / b
    else:
        return "Cannot divide by zero"
def mod(a, b):
    return a % b

print("1.Add \n 2.Sub \n 3.Multiply \n 4.Divide \n 5.Modulo")
choice = int(input("enter your choice :"))
a = int(input("enter first number :"))
b = int(input("enter second number:"))
if choice == 1 :
    print("Result:",add(a, b))
elif choice == 2 :
    print("Result:",sub(a, b))
elif choice == 3 :
    print("Result:",mul(a, b))
elif choice == 4 :
    print("Result:",div(a, b))
else:
    print("Result:",mod(a, b))  


# 6.	Create a function to accept a number & return its factorial

# 7.	Create a function that accept student data, calculate the total & percentage, return total & percentage
def data(name,m1,m2,m3):
    total = m1+m2+m3
    percentage = (total/3)
    return total , percentage
data('ved',89,56,92)
print(f"{total},{percentage}")

# 8.	Create a login function, that accept username & password, if username is ‘admin’ & password is ‘admin@123’
# then return true, else return false
def login(username,password):
    if username == 'admin' and password == 'admin@123':
        return True
    else:
        return False
login('admin','admin@123')
login('adn','admin@123')

l1 = [11,12,13,44,55,66]

print(l1)
print(type(l1))

# for loop
l1[0]=100  # list is mutable

for i,ele in enumerate(l1):
    print(f'{ele}= {i}')
    
print(l1[5])
print(l1[-1])

l1.append(77)
print(l1)

l1.pop(2)
print(l1)

print(l1.pop(0))

l1.insert(1,200)
print(l1)

l1.remove(12)
print(l1)

l1.sort()
print(l1)

l1.sort(reverse=True)
print(l1)

l2 = [1,2,3,[200,400]]
print(l2[3][1]) #list index then element index

print(l2[3])

l2.insert(3,4)
print(l2)

l2[4] = 5
print(l2)

l2.reverse()
print(l2)

l2.extend(l1)
print(l2)

# 1.WAP to remove to find duplicates elements in list,
l1 = [11,23,34,45,45,66,11,54,45]
r = []
for i in l1:
       if i not in r:
            r.append(i)
       else:
            r.remove(i)
print(r)

# 2. WAP to sort the given list
l1.sort()
print(l1)

# 3. WAP to create a list such that new list contains alternate even and odd from given list
l1 = [7,9,4,6,3,1,2]
even = []
odd = []
for num in l1:
    if num % 2 == 0 :
        even.append(num)
    else:
        odd.append(num)
r = []
for i in range(min(len(even),len(odd))):
    r.append(even[i])
    r.append(odd[i])
print(r)


# 4. Write a Python program to get the largest number from a list.
print(max(l1))

# 5. Sample List : ['Red', 'Green', 'White', 'Black', 'Pink', 'Yellow']
#                            Expected Output : ['Green', 'White', 'Black']
l2 = ['Red', 'Green', 'White', 'Black', 'Pink', 'Yellow']
l2.pop(0)
l2.pop(4)
l2.pop(3)
print(l2)

t1 = (11,"hello",113,'a',14)
print(type(t1))

print(t1[0:3])
print(t1[::-2])

def calc(a,b):
    c = a+b
    d = a-b
    return (c,d)

#packing
result = calc(6,2)
print(result)
print(type(result))

#unpacking
sum,sub =result
print(sum)
print(sub)

# Write a Python program to create a tuple.
t1 = ("aksh",24,56,67,'b')
print(t1)
print(type(t1))
# Write a Python program to create a tuple with different data types
# Write a Python program to unpack a tuple in several variables.
person = ("aishwarya",23,"Bidar")
name , age , place = person
print(name)
print(age)
print(place)

# Write a Python program to add an item in a tuple.
t2 = person + ("Karnataka",)
print(t2)

# Write a Python program to convert a tuple to a string.


# Write a Python program to reverse a tuple.
print(t2[::-1])

# Write a Python program to convert a list to a tuple.
l1 = [12,23,34,45,56]
t3 = tuple(l1)
print(t3)
print(type(t3))


# Write a Python program to remove an item from a tuple.
t4 = (76,65,54,43,32,21)
l2 = list(t4)
l2.remove(54)
t5 = tuple(l2)
print(t4) #original
print(t5) #updated



# Write a Python program to slice a tuple.
slice1 = t4[1:5]
slice2 = t4[::2]
slice3 = t4[-2:]
print("slice1 :",slice1)
print("slice2 :",slice2)
print("slice3 :",slice3)

print(len(t4))
print('max',max(t4))


s1 = set()
print(type(s1))
s1 = {21,22,23,24,25,26,27,28}
s1.add(29)
print(s1)
s1.remove(25)
s1.discard(22)
print(s1)
l1 = [12,23,34,54,65,76,87,65,74]
s2 = set(l1)
print(type(s2))
print(len(s2))
print(max(s2))


s1 = {1,2,3,4}
s2 = {3,4,5,6,7}

print(s1.union(s2))
print(s1.difference(s2))
print(s2.difference(s1))
print(s1.intersection(s2))
print(s1.issubset(s2))
print(s2.issuperset(s1))
print(s2.issubset(s1))
print(s1.symmetric_difference(s2))


d1 = {'name' :'shree',
      'age' : 21}

print(d1['age'])

d1['city'] = 'bidar'
print(d1)

del d1['age']
d1['name'] = 'ved'
print(d1)

for k in d1.keys():
    print(k)

for v in d1.values():
    print(v)
    
for k,v in d1.items():
    print(f"{k},{v}")
 


    

