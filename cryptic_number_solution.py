def is_cryptic_number(number):
    # Convert the number to a string to easily access digits
    num_str = str(number)
    
    # Check if the number has at least 3 digits
    if len(num_str) < 3:
        return False
    
    # Check the cryptic number condition
    for i in range(len(num_str) - 2):
        if num_str[i] == num_str[i + 1] == num_str[i + 2]:
            return True
    
    return False

# Example usage
number = 1223
if is_cryptic_number(number):
    print(f"{number} is a cryptic number.")
else:
    print(f"{number} is not a cryptic number.")

number = 1112233
if is_cryptic_number(number):
    print(f"{number} is a cryptic number.")
else:
    print(f"{number} is not a cryptic number.")
