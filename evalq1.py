Python 3.12.1 (tags/v3.12.1:2305ca5, Dec  7 2023, 22:03:25) [MSC v.1937 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> def display_unique_chars(input_string):
...     uppercase_chars = set()
...     lowercase_chars = set()
...     
...     for char in input_string:
...         if char.isupper():
...             uppercase_chars.add(char)
...         elif char.islower():
...             lowercase_chars.add(char)
...     
...     sorted_uppercase = sorted(uppercase_chars)
...     sorted_lowercase = sorted(lowercase_chars)
...     
...     uppercase_output = ', '.join(sorted_uppercase)
...     lowercase_output = ', '.join(sorted_lowercase)
