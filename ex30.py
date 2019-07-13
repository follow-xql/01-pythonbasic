people = 40
cats = 40
trucks = 15

if cats>=people:
    print("We should take the cars.")
elif cats<=people:
    print("We should not take the cars.")
else:
    print("We can't decide.")

if trucks>cats:
    print("That's too many trucks.")
elif trucks<cats:
    print("Maybe we could take the trucks.")
else:
    print("We still can't decide.")

if people>trucks:
    print("Alright,let's just take the trucks.")
else:
    print("Fine,let's stay home then.")
