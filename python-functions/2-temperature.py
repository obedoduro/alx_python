#fahrenheit to celsius
user_input = input()

# Convert the input to an integer (if needed)
try:
    fahrenheit = int(user_input)
except ValueError:
    print("Invalid input. Please enter a valid integer.")


def convert_to_celsius(fahrenheit):

    return (fahrenheit - 32)

temperature_celsius = convert_to_celsius(fahrenheit)
