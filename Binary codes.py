decimal = int(input("Enter a decimal number: "))
binary = ""

# Outer loop: simulate bit positions (optional for learning purposes)
for i in range(decimal.bit_length()):
    remainder = decimal % 2
    binary = str(remainder) + binary
    decimal = decimal // 2

print("Binary representation:", binary)
