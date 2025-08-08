# Advanced Password Generator and Checker
  *This Python script provides a highly customizable password generator and a complexity checker to help you create and assess the strength of your passwords. It offers advanced features like entropy calculation, strength ratings, customizable character sets, and the ability to exclude ambiguous characters for added security.*

## Features
# Password Generation:
> Generate strong passwords with customizable character sets (lowercase, uppercase, digits, special characters).
> Option to exclude ambiguous characters (e.g., 0, O, I, l).
> Specify password length.

# Password Complexity Check:
> Ensure the generated password meets complexity requirements (e.g., must contain at least one lowercase letter, one uppercase letter, one digit, and one special character).

# Password Strength Rating:
> Rate password strength based on entropy (randomness) and uniqueness of characters.
> Entropy provides a quantitative measure of how difficult it is to guess the password.

# Entropy Calculation:
> Calculate the Shannon entropy of a password to determine its randomness.

## Usage
# Generating a Password
You can generate a password with customizable options by calling the generate_password() function.

# Example:
python
Kopieren
Bearbeiten
``generated_password = generate_password(
    length=20, 
    include_upper=True, 
    include_lower=True, 
    include_digits=True, 
    include_special=True
)
print(f"Generated Password: {generated_password}")``

# Checking Password Complexity
After generating a password, you can check its complexity using the check_password_complexity() function.

# Example:
python
Kopieren
Bearbeiten
``complexity_result = check_password_complexity(generated_password)``
``print(f"Password Complexity Check: {complexity_result}")``
This function will check if the password meets the minimum requirements (e.g., length, character types).

# Rating Password Strength
To assess the strength of a password, use the rate_password_strength() function, which gives a strength rating based on entropy.

# Example:
python
Kopieren
Bearbeiten
``strength_info = rate_password_strength(generated_password)``
``print(f"Password Strength: {strength_info['strength']}")``
``print(f"Entropy: {strength_info['entropy']}")``
``print(f"Unique Characters: {strength_info['unique_characters']}")``
``print(f"Password Length: {strength_info['length']}")``
This will output the strength (Weak, Moderate, Strong, Very Strong), entropy, number of unique characters, and the password's length.

## Functions
``generate_password()``
*Generates a random password with customizable options.*

-> Parameters:
  - length (int): Length of the generated password (default: 20).
  - include_upper (bool): Whether to include uppercase letters (default: True).
  - include_lower (bool): Whether to include lowercase letters (default: True).
  - include_digits (bool): Whether to include digits (default: True).
  - include_special (bool): Whether to include special characters (default: True).
  - exclude_ambiguous (bool): Whether to exclude ambiguous characters (e.g., 0, O, I, l) (default: True).

***Returns:**
A randomly generated password string.*

``check_password_complexity()``
*Checks if a password meets the minimum complexity requirements.*

-> Parameters:
*password (str): The password string to be checked.
**Returns:**
A string indicating whether the password meets the requirements or if there are any issues.*

``rate_password_strength()``
*Rates the strength of a password based on its entropy.*

-> Parameters:
*password (str): The password string to be rated.
**Returns:**
A dictionary containing:*
  - entropy (float): The entropy value of the password.
  - unique_characters (int): The number of unique characters in the password.
  - strength (str): A strength rating (Weak, Moderate, Strong, Very Strong).
  - length (int): The length of the password.

``calculate_entropy()``
*Calculates the Shannon entropy of a password to measure its randomness.*

-> Parameters:
*password (str): The password string whose entropy will be calculated.
**Returns:**
The entropy value (float) representing the randomness of the password.*

# Example Output
When you run the script with the sample usage code, you might see output like the following:
> pgsql
> Kopieren
> Bearbeiten
> Generated Password: uT4@*W8pG#qZ2$L5f9b
> Password Complexity Check: Password is strong and meets the requirements!
> Password Strength: Very Strong
> Entropy: 98.96
> Unique Characters: 18
> Password Length: 20

# Security Notes
-> The generated passwords are strong and secure, but always ensure that you store them securely (e.g., using a password manager).
-> Avoid using weak passwords that might be easily guessed.

## License
This project is licensed under the MIT License - see the LICENSE file for details.
