


# Generate the mapping table and replace the data_table variable, look at readme for the code to generate the data 


char_to_number_dict = dict(data_table)
number_to_char_dict = {str(value): key for key, value in data_table}
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
