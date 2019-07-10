def add(a,b):
    print(f"Adding{a} + {b}")
    return a+b
def subtract(a,b):
    print(f"Subtracting {a} - {b}")
    return a-b
def multiply(a,b):
    print(f"Multipling {a} * {b}")
    return a*b
def divide(a,b):
    print(f"Dividing:{a} / {b}")
    return a/b
print("Let's do some math with just functions!")

age = add(30,5)
height = subtract(78,4)
weight = multiply(90,2)
iq = divide(100,2)
print(f"Age:{age},Height:{height},Weight:{weight},Iq:{iq}")
print("Here is a puzzle.")

what = add(age,subtract(height,multiply(weight,divide(iq,2))))
how = divide(iq,multiply(weight,subtract(height,add(age,2))))
print(f"That becomes:{what} Can you do it by hand?")
print(f"That becomes:{how} Can you do it by hand?")
that = subtract(add(divide(34,100),24),1023)
print(that)
print(24+34/100-1023)
