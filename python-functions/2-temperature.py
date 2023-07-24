#fahrenheit to celsius
#convert to censuis and strip
def convert_to_celsius(fahrenheit):

    return ((fahrenheit - 32) * (5 / 9))

temperature_celsius = convert_to_celsius(fahrenheit)
print(temperature_celsius)