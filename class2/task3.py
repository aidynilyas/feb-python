# sum = 0

# for i in range(101):
#     sum += i

# print(sum)

# for i in range(100,1,-1):
#     print(i)

# number = int (input ("Enter a number: "))
# sum = 0

# for i in range (11):
#     sum = number * i
#     print(number, "*", i, "=", sum)


def printNumber(num):
    output = f"{num}"
    if(num%3 == 0):
        output += " foo"

    if (num%5 == 0):
        output += " bar"

    if(num%10 == 0):
        output += " hello"

    print (output)

for i in range (1,101):
    printNumber(i)