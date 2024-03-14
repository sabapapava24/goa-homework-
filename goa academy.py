
# 1. Error: Missing colon after if statement
if x == 5:
    print("x is 5")  # Corrected: Added colon at the end of the if statement

# 2. Error: Undefined variable
# Corrected: Defined variable y before using it
y = 10
print(y)

# 3. Error: IndentationError
# Corrected: Removed extra indentation
print("Indented line")

# 4. Error: Using a reserved keyword as variable name
# Corrected: Used a different variable name
my_var = "hello"

# 5. Error: Invalid syntax for exponentiation
# Corrected: Used parentheses to clarify the order of operations
x = 2**(3**2)

# 6. Error: Division by zero
# Corrected: Avoided division by zero
result = 10 / 2

# 7. Error: Trying to index a non-indexable object
# Corrected: Converted word to a string or list
word = "123"
print(word[0])

# 8. Error: Incorrect function call syntax
# Corrected: Added closing parenthesis for sep
print("Hello", "World", sep="-")

# 9. Error: Incorrect string formatting
# Corrected: Used f-strings or .format() method for string interpolation
name = "Alice"
print(f"Hello, {name}!")

# 10. Error: Missing closing quotation mark
# Corrected: Added a closing quotation mark
message = "This is an unfinished string"

# 11. Error: Misspelled function name
# Corrected: Used math.sqrt() for square root
import math
result = math.sqrt(16)

# 12. Error: Trying to access a non-existent index in a list
# Corrected: Used an existing index within the list bounds
numbers = [1, 2, 3]
print(numbers[2])

# 13. Error: Incorrect usage of the range function
# Corrected: Reversed the range order or provided a negative step value
for i in range(5, 2, -1):
    print(i)

# 14. Error: Using an undefined module
# Corrected: Imported a module that exists
import math

# 15. Error: Incorrect usage of a comparison operator
# Corrected: Used == for comparison
x = 5
if x == 5:
    print("x is equal to 5")

# 16. Error: Incorrect indentation for code block
# Corrected: Indented the code block properly
for i in range(3):
    print(i)

# 17. Error: Using a function before defining it
# Corrected: Defined foo function before calling it
def foo():
    print("foo")

foo()

# 18. Error: Incorrect syntax for accessing dictionary values
# Corrected: Used square brackets to access dictionary values
my_dict = {'a': 1, 'b': 2}
print(my_dict['a'])

# 19. Error: Mismatched parentheses
# Corrected: Added a closing parenthesis
print("Hello world")

# 20. Error: Undefined method for the data type
# Corrected: Used a list instead of an integer and used append method
x = [5]
x.append(6)
print(x)



