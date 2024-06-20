def list_of_int(numbers):
    even_sum = 0
    for number in numbers:
        if number % 2 == 0:
            even_sum += number
    return even_sum

# Example usage:
input_list1 = [1, 2, 3, 4, 5, 6]
input_list2 = [-2, -3, -4, -5]
input_list3 = [1, 3, 5]

print(f"Sum of even numbers in {input_list1} is: {list_of_int(input_list1)}")
print(f"Sum of even numbers in {input_list2} is: {list_of_int(input_list2)}")
print(f"Sum of even numbers in {input_list3} is: {list_of_int(input_list3)}")
