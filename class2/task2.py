numbers = []

def sumNumber(numbers):
    total = sum(numbers)
    print("New total ",total)
    return total

while sumNumber(numbers) < 100:
    numbers.append(int(input("Enter a number:")))
    print(numbers)