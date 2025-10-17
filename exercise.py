#print(dir("rrr"))
#print(help("ddd0".title))

import os

from modules.exercise_functions import parse, convert

text = """
Read a file
Return the todos list form file
"""
print(text)

"""

# this list only include the squares of even numbers
my_list = [x**2 for x in range(1, 6) if x % 2 == 0]
print(my_list)

my_list = ['apple', 'banana', 'cherry', 'date', 'elderberry']

for index, item in enumerate(my_list):
    if index == 2:  # This condition targets the third iteration (index 2)
        print(f"This is the third iteration, the item is: {item}")
    else:
        print(f"Iteration {index+1}: {item}")



for i in range(len(my_list)):
    if i == 2:  # This condition targets the third iteration (index 2)
        print(f"This is the third iteration, the item is: {my_list[i]}")
    else:
        print(f"Iteration {i+1}: {my_list[i]}")


filenames = ["1.Raw data.txt", "2.Reports.txt", "3.Presentations.txt"]
for filename in filenames:
    filename = filename.replace(".", "-", 1)
    print(filename)

filenames = ("1.Raw data.txt", "2.Reports.txt", "3.Presentations.txt")
print(type(filenames)) #tuple
#filenames[1] = 'newfile.txt' return error tuples is immutable

waiting_list = ['sam', 'ben', 'john']
waiting_list.sort()

for index, item in enumerate(waiting_list):
    print(f"{index}.{item.title()}")

waiting_list.reverse()
for index, item in enumerate(waiting_list):
    print(f"{index}.{item.title()}")

buttons = [('John', 'Sen', 'Morro'), ('Lin', 'Ajay', 'Filip')]
for first, second, third in buttons:
    print(first, second, third)


user_input = input("Please Enter your name: ")
file = open("files/members.txt", "r")
content = file.readlines()
file.close()
content.append(user_input)
file = open("files/members.txt", "w")
file.writelines(content)
file.close()


a = "I'a a very" \
    " long string" \
    " very very long"
print(a)

filenames = ("doc.txt", "reports.txt", "presentations.txt")
contents = ["This is the first row in first file"
            "This is the second row in first file."
            "This is the third row in first file.",
            "This is the second file content",
            "This is the third file content"]

for filename, content in zip(filenames, contents):
    path = f"files/{filename}"
    file = open(path, "w")
    file.writelines(content)
    file.close()


words = []
filenames = ("doc.txt", "reports.txt", "presentations.txt", "members.txt")
for filename in filenames:
    path = f"files/{filename}"
    file = open(path, "r")
    content = file.readlines()
    file.close()

    for sentense in content:
        all_in_sentense = sentense.split(' ')
        for word in all_in_sentense:
            if word.startswith("s"):
                words.append(word)
print(words)


filenames = ("1.doc", "2.reports", "3.presentations")
formatted_filenames = [item.replace('.','-',1) + '.txt' for item in filenames]
print(formatted_filenames)

user_entries = ['10', '19.1', '20']
floats = [float(item) for item in user_entries]
print(sum(floats))


date = input("Enter today's date:")
mood = input("How do you rate your mood today from 1 to 10?")
journal = input("Let your thoughts flow: \n")

with open(f"files/{date}.txt", "w") as file:
    file.write(f"Mood rate is {mood} \n")
    file.write(journal)
    
with open(f"files/2025-10-13.txt", "r") as file:
    content = file.read()
    print(content)
    print(len(content))


password = input("Enter your password:")
result = {'length': True, 'upper': True, 'digit': True, 'empty': True }
if password == "":
    print("Password is empty")
    result['empty'] = False
if len(password) < 8:
    result['length'] = False
    print("Password must be at least 8 characters long")
if not any(char.isupper() for char in password):
    result['upper'] = False
    print("Password must be at least one uppercase letter")
if not any(char.isdigit() for char in password):
    result['digit'] = False
    print("Password must be at least one digit")

if all(result.values()):
    print("The password is strong")


def strength(password):
    valid = True
    if password == "":
        valid = False
    if len(password) < 8:
        valid = False
    if not any(char.isupper() for char in password):
        valid = False
    if not any(char.isdigit() for char in password):
        valid = False
    
    if valid:
        return"Strong Password"
    return "Weak Password"
    

try:
    "a" + 2
except TypeError:
    print("Cannot add number to string.")

filenames = ["report.txt", "downloads.txt", "success.txt", "folders.txt"]
for name in filenames:
    dot_index = name.rfind('.')
    print(name[:dot_index])

try:
    waiting_list = ["john", "marry"]
    name = input("Enter name: ")

    number = waiting_list.index(name)
    print(f"{name}'s turn is {number}")
except ValueError:
    print("Sorry, the name you entered is not valid")

try:
    total_value = float(input("Enter total value: "))
    value = float(input("Enter value: "))

    print(f"That is {value/total_value * 100} %")
except ZeroDivisionError:
    print("Total value can not be 0")
except Exception as e:
    # 'e' is the exception object
    exception_message = str(e)
    print(f"An error occurred: {exception_message}")


def get_maximum():
    celsius = [14, 15.1, 12.3]
    maximum = max(celsius)
    return maximum


celsius = get_maximum()
fahrenheit = celsius * 1.8 + 32
print(fahrenheit)


def get_average():
    with open(f"files/doc.txt", "r") as file:
        data = file.readlines()

    # get lines from the second line
    values = data[1:]

    # remove new line and convert each value to float
    values = [float(i.replace('\n', '')) for i in values]
    return sum(values) / len(values)


average = get_average()
print(average)

"""
"""
# decoupling
from modules import  exercise_functions as ef

feet_inches_input = input("Enter feet and inches: ")
f,i = ef.parse(feet_inches_input)
converted: float = ef.convert(f, i)

print(f"{f} feet and {i} inches is equal to {converted} meters")
if converted > 1:
    print("Kid can use the slide")
else:
    print("Kis is too small")
"""
"""
import glob

myfiles = glob.glob("files/*.txt")
for filename in myfiles:
    print(filename)

"""

"""
#working with csv files
import  csv

with open(f"files/weather.csv", "r") as file:
    reader = csv.reader(file)
    data = list(reader)

city = input("Enter a city: ")
for row in data[1:]:
    if row[0] == city:
        print(row[1])

"""
"""
import shutil

shutil.make_archive("files", "zip", "files")
shutil.copyfile("files.zip", "files/output.zip")
"""

"""
import  webbrowser

user_term = input("Enter a term: ").replace(' ', '+')
webbrowser.open(f"https://google.com/search?q={user_term}")
"""

"""
import json

quiz_questions = []
with open("files/quiz.json", "r") as file:
    content = file.read()
    if content:
        quiz_questions = json.loads(content)['quiz']

correctAnswers = 0;
for question in  quiz_questions:
    print(question['question'])
    for option in question['options']:
        print(option)
    answer = input("Enter your answer: ")
    if answer == 'stop':
        break
    if answer == question['correctAnswer']:
        print("Correct!")
        correctAnswers = correctAnswers + 1
    else:
        print(f"Wrong! The correct answer is: {question['correctAnswer']}")

print(f"You answered {correctAnswers} correctly from {len(quiz_questions)} questions")
"""


def parse_dic(user_input):
    """Extract the values split by a comma in a string
    and return the two values via a dictionary.
    """
    # Get the two values in a list
    parts = user_input.split(",")

    # Store the two values in variables
    lower_bound = int(parts[0])
    upper_bound = int(parts[1])

    # Inject the values in a dictionary
    return {"lower_bound": lower_bound, "upper_bound": upper_bound}

import random

user_input = input("Enter a lower bound and an upper bound divided a comma (e.g., 2,10)")
parsed = parse_dic(user_input)
rand = random.randint(parsed['lower_bound'], parsed['upper_bound'])

print(rand)