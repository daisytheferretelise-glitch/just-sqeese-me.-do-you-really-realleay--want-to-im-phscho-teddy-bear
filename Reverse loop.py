print("Bob can count the digits in your number—just enter it!")

# Ask the user to enter a number
number = int(input("Enter a number: "))

# Convert to positive if it's negative
number = abs(number)

# Initialize digit count
count = 0

# Handle the case where the number is 0
if number == 0:
    count = 1
else:
    # Use a while loop to count digits
    while number != 0:
        number = number // 10  # Remove the last digit
        count += 1

# Display the result
print("Bob says the total number of digits is:", count)
