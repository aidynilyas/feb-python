while True:
    age=int(input("Enter your age: "))

    if(age < 13 and age > 0):
        print("You are not allowed")
    elif (age >= 13 and age < 18):
        print("You need a guardian")
    elif (age <= 0):
        print("what the fuck.")
    else:
        print("You are welcome")