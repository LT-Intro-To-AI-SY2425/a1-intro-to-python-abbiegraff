# Complete your individualized AI problems here

def fizbuzz(input_num):
    if(input_num%3==0):
        if(input_num%5==0):
            return 'FizzBuzz'
        return 'Fizz'
    elif(input_num%5==0):
        return 'Buzz'
    else:
        return input_num

assert fizbuzz(1) == 1, "fizzbuzz 1 test"
assert fizbuzz(3) == "Fizz", "fizzbuzz 3 test"
assert fizbuzz(4) == 4, "fizzbuzz 4 test"
assert fizbuzz(5) == "Buzz", "fizzbuzz 5 test"
assert fizbuzz(6) == "Fizz", "fizzbuzz 6 test"
assert fizbuzz(15) == "FizzBuzz", "fizzbuzz 15 test"

#Sum of Two Numbers
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))

sum_of_numbers = num1 + num2 
print(f"The sum of {num1} and {num2} is {sum_of_numbers}")

#Convert Temperature between Celsius and Fahrenheit
def convert_temperature(value, scale_from, scale_to):
    """
    Conver temperature between Celsius and Fahrenheit.
    :param value: The temperature value to convert.
    :param scale_from: The current scale of the temperature ('C' or 'F').
    :param scale_to: The scale to convert the temperature to ('C' or 'F').
    :return: The converted temperature. 
    """
    if scale_from == scale_to: 
        return value 
    if scale_from == 'C' and scale_to == 'F':
        return (value * 9/5) + 32
    elif scale_from == 'F' and scale_to == 'C':
        return (value - 32) * 5/9
    else:
        raise ValueError("Invalid scale. Use 'C' for Celsius or "F" for Fahrenheit.")
    
    temp_in_celsius = 25 
    temp_in_fahreneit = convert_temperature(temp_in_celsius, 'C', 'F')
    print(f"{temp_in_celsius}°C is {temp_in_fahrenheit}°F")

    temp_in_fahrenheit = 77
    temp_in_celsius = convert_temperature(temp_in_fahrenheit, 'F', 'C')
    print(f"{temp_in_fahrenheit}°F is {temp_in_celsius}°C")

#Greeting 
name = input("What is your name? ")
print(f"Hello, {name}! Nice to meet you.")
    