
# Crybaby

Crybaby is a Python encryption tool that uses unique hashing techniques to convert your sensitive information into a numerical format. With its innovative approach, Crybaby provides a clever way to store data securely as numbers. 

## How It Works

Crybaby utilizes a custom character-to-number mapping table to generate unique hashes based on your input data and a provided key. The encryption process involves:


1. **Character Mapping**: Each character is mapped to a unique number. You can structure your mapping table in any way you want.
2. **Salting**: A salt is generated based on the key and its length.
3. **Hash Generation**: The data is processed mathematically to create a secure hash.

## Generating the Character-to-Number Mapping Table

Before using Crybaby, you need to generate a character-to-number mapping table. This table is essential for the encryption and decryption processes. Follow the steps below to create your mapping table:

1. **Open the `crybaby.py` file** in your preferred code editor.
2. **Locate the `data_table` variable** in the code, where the character mappings are defined.
3. **Use the following code snippet** to generate a unique four-digit number for each character:

```python
import random

# Function to generate a unique mapping table
def generate_data_table():
    characters = list("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!\"#$%&'()*+,-./:;<=>?@[\\]_^`{|}~ ")
    data_table = []

    for char in characters:
        unique_number = random.randint(1000, 9999)  # Generate a random four-digit number
        data_table.append((char, unique_number))
    
    return data_table

# Generate the mapping table
data_table = generate_data_table()
```

4. **Add the generated mapping table** to your `crybaby.py` file. The `data_table` variable should look like this:

```python
data_table = [
    # Add your generated mappings here
    ('a', 1234), ('b', 5678), # Example mappings
    # ...
]
```

## Installation

To use Crybaby, simply clone the repository and install any necessary dependencies. Make sure you have Python installed.

```bash
git clone https://github.com/YourUsername/Crybaby.git
cd Crybaby
```

## Usage

1. Import the Crybaby module in your Python script.

```python
import crybaby
```

2. Encrypt data using the `encrypt` method.

```python
# Example usage
data = "YourSensitiveData"
key = "YourSecretKey"

# Encrypt the data
encrypted_data = crybaby.encrypt(data, key)
print("Encrypted Data:", encrypted_data)
```

3. Decrypt data using the `decrypt` method.

```python
# Decrypt the data
decrypted_data = crybaby.decrypt(encrypted_data, key)
print("Decrypted Data:", decrypted_data)
```

## Example

Here’s a complete example of how to use Crybaby:

```python
import crybaby

data = "MySecretPassword"
key = "MySecretKey"

# Encrypt
encrypted_data = crybaby.encrypt(data, key)
print("Encrypted Data:", encrypted_data)

# Decrypt
decrypted_data = crybaby.decrypt(encrypted_data, key)
print("Decrypted Data:", decrypted_data)
```

## Disclaimer

Crybaby is intended for educational purposes and fun experimentation. While it provides a way to obscure your data, it should not be used for securing highly sensitive information.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
