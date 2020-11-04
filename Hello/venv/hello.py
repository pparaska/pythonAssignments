"""
x = "Hello World"
y = '   hello , World  '

print(x.upper())
print(y.lower())
print(y.strip())
print(y.split(','))
print(x.islower())
print(y.isupper())
print(y * 10)

x = -100
if x < 200 or x < 0:
    print("Value of x is", x)
if x >=100:
    print("x is positive")
else:
    print("x is negative")
print("finish.....")


num = 1
sum = 0

while num != 0 :
    num = float(input("Enter a number : "))
    sum = sum + num
    print("Sum = ", sum)

else:
    print("Finished sum...")


i = 0
while True :
    print("Value of i is = ", i)
    i = i + 1
    break;
print("Finished while loop")
"""

def student(name = 'Unknown', age = 0, **marks):
    print("Name is : ", name)
    print("Age is : ", age)
    print("marks : ", marks)
    for key,value in marks.items():
        print(key,value)

student('Poonam', 23, Eng =80, Maths= 99, Science=97)


