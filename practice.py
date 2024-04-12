'''
num1 = int(input("Enter a number: "))
num2 = int(input("Enter 2nd number: "))
num3 = int(input("Enter 3rd number: "))
if (num1 > num2 and num1 > num3):
    print(num1," is largest among three integers.")
elif (num2 > num1 and num2 > num3):
    print(num2," is largest among three integers.")
else:
    print(num3," is largest among three integers.")
    '''

'''
name_1st = ["Akash","Jaya"]
tup = ("item_1", 0.5,name_1st)
name_1st.append("khan")
print(tup)
num = int(input("Enert a number: "))
print(num + 1)
'''
'''
def fizz_buzz(input):
    if input % 3 == 0 and input % 5 == 0:
        return "FizzBuzz"
    if input % 3 == 0:
        return "Fizz"
    if input % 5 == 0:
        return "Buzz"
print(fizz_buzz(15))
'''
# Function to find factorial
'''
def factorial(n):
  fact = 1
  for i in range(1, n+1):
    fact *= i
  print(fact)
num = int(input("Enter a number: "))
factorial(num)
'''

# Fuction to print the length of a list
'''
list = [1,2,3,5,8]
Name = "Khalid Nawaz"
def list_len(cities):
  print(len(cities))
list_len(list)
list_len(Name)
'''

# Function to print the elements of a list
'''
list = [1,3,5,34,23,25,25,26]
def list_elements(element):
    for element in list:
        print(element, end = " ")
list_elements(list)
'''

'''
def print_all(*args):
  for item in args:
    print(item)

print_all("Hello", "World", 10)  # Pass multiple arguments
'''

# Simple Statistics with *args
'''
def calculate_stats(*numbers):
    if len(numbers) == 0:
        return None, None, None
    minimum = min(numbers)
    maximam = max(numbers)
    average = sum(numbers) / len(numbers)
    return minimum, maximam, average
data = [3,56,23,12]
min_value, max_value, average_value = calculate_stats(*data)
print(f"Minimum: {min_value} Maximam: {max_value} Average: {average_value}")
'''

# Sum of all even numbers in a data 
'''
def sum_of_even(*numbers):
    sum = 0
    for item in numbers:
        if item % 2 == 0:
            sum += item
        else:
            continue
    return sum
data = [1,2,3,4,5,6]
sum_even = sum_of_even(*data)
print(f"Sum of Even Numbers: {sum_even}")
'''

# Display info using *args and **kwargs

def display_info(*name, **info):
    age = info.get("age")
    message = f"Name: {name}"
    if age:
       message += f", Age: {age}"
    print(message)
display_info("Khalid Nawaz")
display_info("Khalid Nawaz", age = 30)
print("python"[-1])