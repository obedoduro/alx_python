#fahrenheit to celsius
fahrenheit = -459.67



def approximate_float(fahrenheit):
    # Convert the number to a string
    number_str = str(fahrenheit)

    # Remove trailing zeros after the decimal point
    approximated_str = number_str.rstrip('0').rstrip('.')

    # Convert back to float (if needed)
    if '.' in approximated_str:
        approximated_number = float(approximated_str)
    else:
        approximated_number = int(approximated_str)
        print(approximated_number)
    
    return approximated_number

def convert_to_celsius(temperature):
    

 return ((temperature - 32) * (5 / 9))

temperature =  approximate_float(fahrenheit) 
temperature_celsius = convert_to_celsius(temperature)
print(temperature_celsius)