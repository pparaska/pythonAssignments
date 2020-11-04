result = None

a = float(input('Number1 :'))
b = float(input('Number2 :'))

try:
    result = a / b
except ZeroDivisionError as e:
    print("Exception: ", e)
else:
    print("printing else")
finally:
    print("printing finally")

print(result)
