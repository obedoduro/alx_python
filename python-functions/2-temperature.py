def approximate_float(number):
    # Convert the number to a string
    number_str = str(number)

    # Remove trailing zeros after the decimal point
    approximated_str = number_str.rstrip('0').rstrip('.')

    # Convert back to float 
    if '.' in approximated_str:
        approximated_number = float(approximated_str)
    else:
        approximated_number = int(approximated_str)

    return approximated_number
