# Davis Burke, 20101583, 11/2/23
largest = None
smallest = None
while True:
    num = input("Enter a number: ")

    if num == "done":
        break
    try:
        num2 = int(num)
    except:
        print("Invalid input")

    if num2 / 1 == False:
        print("Number error")
        continue

    if smallest is None or num2 < smallest:
        smallest = num2

    if largest is None or num2 > largest:
        largest = num2

slargest = str(largest)
ssmallest = str(smallest)
print("Maximum is " + slargest)

print("Minimum is " + ssmallest)
