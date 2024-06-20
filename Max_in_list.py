def find_maximum(numbers):
    if not numbers:
        raise ValueError("The list is empty")
    
    max_number = numbers[0]
    for number in numbers:
        if number > max_number:
            max_number = number
    return max_number

# Example usage:
input_list = [3, 5, -2, 10, -6]
max_number = find_maximum(input_list)
print(f"The maximum number in the list is: {max_number}")
