sum = 0
for i in range(5):
    while True:
        try:
            inp = int(input("Please enter an integer: "))
            sum += inp
            break
        except ValueError:
            print("Invalid input. Please enter an integer.")
print("The sim is:", sum)


