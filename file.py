def double_stuff(input_list):
    for i, v in enumerate(input_list):
        input_list[i] = v*2
    return input_list
list = [2.5,4.3,8.6,10,12,14,16]
result_list = double_stuff(list)

print(result_list)

# Test Case 1: List with Integers
int_list = [2, 4, 8, 10, 12, 14, 16]
result_int_list = double_stuff(int_list)
print(result_int_list)

# Test Case 2: List with Float Values
float_list = [2.5, 4.3, 8.6, 10.0, 12.8, 14.2, 16.1]
result_float_list = double_stuff(float_list)
print(result_float_list)