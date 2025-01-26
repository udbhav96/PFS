#Try 1(seen)
def int_to_list_alternative(number):
    is_negative = False
    if number < 0:
        is_negative = True
        number = -number
    
    result = []
    
    while number > 0:
        digit = number % 10
        result.append(digit)  # Append the digit at the end of the list
        number = number // 10
    
    if not result:
        result.append(0)
    
    if is_negative:
        result.insert(0, '-')  # Add the negative sign if needed
    
    return result[::-1]  # Reverse the list to get digits in correct order
