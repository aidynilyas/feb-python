import random


age = int(input("What is your age: "))

if age < 13:
    print("You are a child")
elif age >= 13 and age < 18:
    print("You are a teenager")
elif age >= 18 and age < 65:
    print("You are an adult")
else:
    print("You are an elder")

total = random.randint(15, 150) 
tip_input = int(input(f"The total is ${total}\nEnter the tip: $"))

tipAmount = tip_input / total
tipAmount *= 100

if tipAmount < 15:
    print(f"This is okay tip - %{tipAmount}") 
elif tipAmount >= 18 and tipAmount < 20: 
    print(f"This is good tip - %{tipAmount}") 
else: 
    print(f"This is great tip - %{tipAmount}") 