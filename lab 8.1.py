
#Task Description #1 (Password Strength Validator – Apply AI in
#Security Context)
#• Task: Apply AI to generate at least 3 assert test cases for
#is_strong_password(password) and implement the validator
#function.
#• Requirements:
#o Password must have at least 8 characters.
#o Must include uppercase, lowercase, digit, and special
#character.
#o Must not contain spaces.
#Example Assert Test Cases:
#assert is_strong_password("Abcd@123") == True
#assert is_strong_password("abcd123") == False
#assert is_strong_password("ABCD@1234") == True
#Expected Output #1:
#• Password validation logic passing all AI-generated test cases.
import re   
def is_strong_password(password):
    if len(password) < 8:
        return False
    if not re.search(r'[A-Z]', password):
        return False
    if not re.search(r'[a-z]', password):
        return False
    if not re.search(r'[0-9]', password):
        return False
    if not re.search(r'[@$!%*?&]', password):
        return False
    if ' ' in password:
        return False
    return True
# Assert Test Cases
assert is_strong_password("Abcd@123") == True
assert is_strong_password("abcd123") == False
assert is_strong_password("Abcdefg") == False
assert is_strong_password("Abcdefg1") == False

print("All test cases passed!")
#Task Description #2 (Number Classification with Loops – Apply
#AI for Edge Case Handling)
#• Task: Use AI to generate at least 3 assert test cases for a
#classify_number(n) function. Implement using loops.
#• Requirements:
#o Classify numbers as Positive, Negative, or Zero.
#o Handle invalid inputs like strings and None.
#o Include boundary conditions (-1, 0, 1).
#Example Assert Test Cases:
#assert classify_number(10) == "Positive"
#assert classify_number(-5) == "Negative"
#assert classify_number(0) == "Zero"
#Expected Output #2:
#• Classification logic passing all assert tests.
#we have enter the input 

def classify_number(n):
    if n is None or isinstance(n, str):
        return "Invalid input"
    if n > 0:
        return "Positive"
    elif n < 0:
        return "Negative"
    else:
        return "Zero"
# Assert Test Cases
assert classify_number(10) == "Positive"
assert classify_number(-5) == "Negative"
assert classify_number(0) == "Zero"
assert classify_number("abc") == "Invalid input"
assert classify_number(None) == "Invalid input" 
print("All test cases passed!")
#Task Description #3 (Anagram Checker – Apply AI for String
#Analysis)
#• Task: Use AI to generate at least 3 assert test cases for
#is_anagram(str1, str2) and implement the function.
#• Requirements:
#o Ignore case, spaces, and punctuation.
#o Handle edge cases (empty strings, identical words).
#Example Assert Test Cases:
#assert is_anagram("listen", "silent") == True
#assert is_anagram("hello", "world") == False
#assert is_anagram("Dormitory", "Dirty Room") == True
#Expected Output #3:
#• Function correctly identifying anagrams and passing all AI-
#generated tests.
import re
def is_anagram(str1, str2):
    # Remove spaces and punctuation, and convert to lowercase
    str1 = re.sub(r'[\W_]', '', str1).lower()
    str2 = re.sub(r'[\W_]', '', str2).lower()
    
    # Check if sorted characters are the same
    return sorted(str1) == sorted(str2)

# Assert Test Cases
assert is_anagram("listen", "silent") == True
assert is_anagram("hello", "world") == False
assert is_anagram("Dormitory", "Dirty Room") == True
assert is_anagram("", "") == True
assert is_anagram("abc", "abc") == True
print("All test cases passed!")
#Task Description #4 (Inventory Class – Apply AI to Simulate Real-
#World Inventory System)
#• Task: Ask AI to generate at least 3 assert-based tests for an
#Inventory class with stock management.
#• Methods:
#o add_item(name, quantity)
#o remove_item(name, quantity)
#o get_stock(name)
#Example Assert Test Cases:
#inv = Inventory()
#inv.add_item("Pen", 10)
#assert inv.get_stock("Pen") == 10
#inv.remove_item("Pen", 5)
#assert inv.get_stock("Pen") == 5
#inv.add_item("Book", 3)
#assert inv.get_stock("Book") == 3
#Expected Output #4:
#• Fully functional class passing all assertions.
class Inventory:
    def __init__(self):
        self.stock = {}
    
    def add_item(self, name, quantity):
        if name in self.stock:
            self.stock[name] += quantity
        else:
            self.stock[name] = quantity
    
    def remove_item(self, name, quantity):
        if name in self.stock and self.stock[name] >= quantity:
            self.stock[name] -= quantity
        else:
            raise ValueError("Not enough stock to remove")
    
    def get_stock(self, name):
        return self.stock.get(name, 0)
# Assert Test Cases
inv = Inventory()
inv.add_item("Pen", 10)
assert inv.get_stock("Pen") == 10

inv.remove_item("Pen", 5)
assert inv.get_stock("Pen") == 5

inv.add_item("Book", 3)
assert inv.get_stock("Book") == 3
print("All test cases passed!")
#Task Description #5 (Date Validation & Formatting – Apply AI for
#Data Validation)
#• Task: Use AI to generate at least 3 assert test cases for
#validate_and_format_date(date_str) to check and convert
#dates.
#• Requirements:
#o Validate "MM/DD/YYYY" format.
#o Handle invalid dates.
#o Convert valid dates to "YYYY-MM-DD".
#Example Assert Test Cases:
#assert validate_and_format_date("10/15/2023") == "2023-10-15"
#assert validate_and_format_date("02/30/2023") == "Invalid Date"
#assert validate_and_format_date("01/01/2024") == "2024-01-01"
#Expected Output #5:
#• Function passes all AI-generated assertions and handles edge
#cases
from datetime import datetime
def validate_and_format_date(date_str):
    try:
        date_obj = datetime.strptime(date_str, "%m/%d/%Y")
        return date_obj.strftime("%Y-%m-%d")
    except ValueError:
        return "Invalid Date"
# Assert Test Cases
assert validate_and_format_date("10/15/2023") == "2023-10-15"
assert validate_and_format_date("02/30/2023") == "Invalid Date"
assert validate_and_format_date("01/01/2024") == "2024-01-01"
assert validate_and_format_date("13/01/2023") == "Invalid Date"
assert validate_and_format_date("00/10/2023") == "Invalid Date"
print("All test cases passed!")