limit=(int(input("Enter limit: ")))

first = 0
second = 1
sum = first + second

while (sum) < limit:
    print (sum)
    sum = first + second
    first = second
    second = sum