#Try 1 (seen)
def int_to_str(number):
    is_negative = False
    
    
    if number < 0:
        is_negative = True
        number = -number

    result = ""
    while number > 0:
        digit = number % 10  
        char = chr(digit + ord('0'))
        result = char + result  
        number //= 10
    
   
    if result == "":
        result = "0"
    
    # Add negative sign if needed
    if is_negative:
        result = "-" + result
    
    return result
