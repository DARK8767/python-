#QUESTION 1
calculate_area = lambda side: side ** 2

side = int(input('Enter the side of square : '))
area = calculate_area(side)
print(f"AREA OF SQUARE WITH SIDE {side} is : ",area)


#QUESTION 2
def sum_of_digits(number):
    sum_digits = 0
    while number > 0:
        digit = number % 10  # Get the last digit
        sum_digits += digit  # Add the digit to the sum
        number //= 10  # Remove the last digit
    return sum_digits

input_number = int(input("Enter a number: "))
digit_sum = sum_of_digits(input_number)
print("Sum of digits:", digit_sum)