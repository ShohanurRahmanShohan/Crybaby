# Replace the data_table with the following code to generate a unique mapping:
# 
# import random
# 
# def generate_mapping_table():
#     """Generate a character-to-number mapping table."""
#     mapping_table = []
#     unique_numbers = set()
# 
#     # Define the range of characters you want to include
#     for char in range(32, 127):  # ASCII characters from space (32) to ~ (126)
#         while True:
#             # Generate a unique 4-digit number
#             number = random.randint(1000, 9999)
#             if number not in unique_numbers:
#                 unique_numbers.add(number)
#                 mapping_table.append((chr(char), number))
#                 break
# 
#     return mapping_table
# 
# # Generate the mapping table and replace the data_table variable
# data_table = generate_mapping_table()

# Example function to demonstrate encryption and decryption (remains unchanged)
def get_concatenated_number_from_string(input_string):
    concatenated_number_str = ''.join(str(char_to_number_dict.get(char, '')) for char in input_string)
    return int(concatenated_number_str) if concatenated_number_str else None

def reverse_concatenated_number(concatenated_number):
    concatenated_number_str = str(concatenated_number)
    original_string = ''
    for i in range(0, len(concatenated_number_str), 4):
        chunk = concatenated_number_str[i:i + 4] 
        if chunk in number_to_char_dict:
            original_string += number_to_char_dict[chunk]  
    return original_string

def encrypt(data, key):
    Key = get_concatenated_number_from_string(key)
    Data = get_concatenated_number_from_string(data)
    salt = int(Key) * len(key)
    hash_value = int(Data) * salt
    return hash_value

def decrypt(data, key):
    Key = get_concatenated_number_from_string(key)
    if Key is None or Key == 0:
        print("Key is invalid (None or zero).")
        return None
    try:
        salt = int(Key) * len(key)
        Data = int(data) // salt
    except ValueError:
        print("Data is not a valid number.")
        return None
    return reverse_concatenated_number(str(Data))

# Note: Make sure to replace the data_table with the generated mapping table in your implementation.
