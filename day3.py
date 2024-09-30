# count = 1

# while count > 100:
#     print(count)
#     count += 1
number = int(input("Enter a number: "))

if number > 0:
    print("The number is positive.")
elif number:
    print("The number is negative.")
else:
    print("The number is zero.")
if number > 0:
    for i in range (1,number +1):
        print(i)