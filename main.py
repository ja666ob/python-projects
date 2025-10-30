'''
questions = ("How many elements are there in periodic table?: ",
             "Which animal lays the largest eggs?: ",
             "What is the most abundant gas in Earth's atmosphere?: ",
             "How many bones are in the human body?: ",
             "Which planet in the solar system is the hottest?: ")

options = (("Α. 116", "B. 117", "С. 118", "D. 119"),
           ("A. Whale", "B. Crocodile", "C. Elephant", "D. Ostrich"),
           ("A. Nitrogen", "B. Oxygen", "C. Carbon-Dioxide", "D. Hydrogen"),
           ("Α. 206", "В. 207", "С. 208", "D. 209"),
           ("A. Mercury", "B. Venus", "C. Earth", "D. Mars"))

answers = ("C","D","A","A","B")
guesses = []
score = 0
question_num =  0

for question in questions:
    print("------------------------")
    print(question)

    for option in options[question_num]:
        print(option)

    guess = input("Guess a Letter: ").upper()
    guesses.append(guess)

    if guess == answers[question_num]:
        print("Correct!")
        score += 1
    else:
        print("Incorrect!")
        print(f"The correct answer is {answers[question_num]}")

    question_num += 1
print("---------RESULT---------")
print(f"You answered {score} out of {len(questions)} questions.")

budget = float(input("Enter Your Budget: "))
print("apple/bread/milk/eggs/cheese")

cart = []
total = 0
price = (1.50,2.00,3.25,2.50,5.00)

while True:
    pick = input("Which food do you want to pick?: ")
    if pick == "checkout":
        break
    else:
        if budget <= 0:
            print("Sorry your Budget is not enough")
            print("Please Check out now")
        elif pick == "apple":
            budget -= price[0]
            total += price[0]
            cart.append(pick)
        elif pick == "bread":
            budget -= price[1]
            total += price[1]
            cart.append(pick)
        elif pick == "milk":
             budget -= price[2]
             total += price[2]
             cart.append(pick)
        elif pick == "eggs":
            budget -= price[3]
            total += price[3]
            cart.append(pick)
        elif pick == "cheese":
            budget -= price[4]
            total += price[4]
            cart.append(pick)
        elif pick == "cart".lower():
            print(f"Your cart: {cart}")
            print(f"Your current budget is ${budget}")

print("---------YOUR GROCERY--------")
print(f"Your orders are {cart}")
print(f"The total amount of your grocery cart is {total} ")
print(f"Your remaining budget is ${budget}")


try:
    budget = float(input("Enter Your Budget: $"))
except ValueError:
    print("Invalid input. Please enter a number.")
    exit()
menu = {
    "apple": 1.50,
    "bread": 2.00,
    "milk": 3.25,
    "eggs": 2.50,
    "cheese": 5.00
}

cart = []
total = 0

print("\n--- Welcome to the Grocery Store! ---")

while True:
    print("\n--- Available Items ---")

    for item, price in menu.items():
        print(f"- {item.capitalize()}: ${price:.2f}")

    print(f"\nYour remaining budget is: ${budget:.2f}")

    pick = input("What do you want to buy? (type 'checkout' to finish) ").lower()

    if pick == "checkout":
        break

    if pick in menu:
        price_of_item = menu[pick] # Get the price from the dictionary

        if budget >= price_of_item:
            cart.append(pick)
            budget -= price_of_item
            total += price_of_item
            print(f"'{pick.capitalize()}' added to your cart.")
        else:
            print(f"Sorry, you don't have enough money for {pick.capitalize()}.")

    else:
        print("That item is not available. Please choose from the list.")

# --- Final Output ---
if cart:
    print("\n" + "-" * 20)
    print("--- YOUR RECEIPT ---")
    for item in set(cart):
        qty = cart.count(item)
        print(f"{item} x{qty} - ${menu[item] * qty:.2f}")

    print(f"\nTotal: ${total:.2f}")
else:
    print("\nYour cart is empty.")
print(f"Your remaining budget is: ${budget:.2f}")
print("-" * 20)

import random

options = ("rock", "paper", "scissors")

player_score = 0
computer_score = 0
running = True
trashtalk = True

ign = input("Enter your IGN: ")
print(f"Welcome, {ign}!")
print()

while running:
    computer = random.choice(options)
    pick = input("Enter a choice (rock, paper, scissors): ")

    if pick not in options:
        print("Invalid input. Please choose from the list.")
        print()

    else:
        print(f"\n{ign}: {pick}")
        print(f"Computer: {computer}")
        print()

        if pick == computer:
            print("It's a draw.")

        elif pick == "paper" and computer == "scissors":
                computer_score += 1
                print("Computer wins!")

        elif pick == "scissors" and computer == "rock":
                computer_score += 1
                print("Computer wins!")

        elif pick == "rock" and computer == "paper":
               computer_score += 1
               print("Computer wins!")

        else:
            player_score += 1
            print(f"{ign} wins!")

        while trashtalk:
            if player_score == 1 and computer_score == 0:
                print(f"{ign}: 1 - sorry BOBO")
                trashtalk = False

            elif computer_score == 1 and player_score == 0:
                print("Computer: 1 - sorry BOBO")
                trashtalk = False

        print()
        print(f"----SCORE----")
        print(f"Computer: {computer_score}")
        print(f"{ign}: {player_score}")

    if player_score == 2:
        print("AND THE WINNER IS")
        print(f"{ign}!!!")

    elif computer_score == 2:
        print("AND THE WINNER IS")
        print("COMPUTER!!!")

    if computer_score == 2 or player_score == 2:
        asking = True
        while asking:
            play_again = input(f"\n{ign}, Would you like to play again? (yes/no): ").lower()

            if play_again == "no":
                print(f"Thank you {ign} for playing.")
                asking = False
                running = False

            elif play_again == "yes":
                computer_score = 0
                player_score = 0
                print("Okay, One More Game!")
                print()
                asking = False
                continue
            else:
                print("Sorry, I didn't understand that. Please try again.")

def divide(x, y):
   z = x / y
   return z
print(divide(10,2))

def create_name(first, last):
    first = first.capitalize()
    last = last.capitalize()
    return f"{first} {last}"

print(create_name("Jacob","Manuel"))

def display_name(*args):
    for arg in args:
        print(arg, end=" ")

display_name("Jacob", "Manuel")

names = ["Jacob", "Manuel","asd"]
for name in names:
    print(name)
fruits = ["apple","banana","mango"]
fruit = [fruit for fruit in fruits]
print(fruits)

def show_balance(balance):
    print(f"Your balance is: ${balance:.2f}")
    print()

def deposit(balance):
    amount = float(input("Enter your deposit: "))
    return amount

def withdraw(balance):
    amount = float(input("Enter your withdrawal: "))
    if amount > balance:
        print("You don't have enough money.")
        return 0
    elif amount < 0:
        print("Amount must be greater than 0.")
        return 0
    else:
        return amount

def main():
    balance = 0
    is_running = True

    while is_running:
        print("Banking Program")
        print("1.Show Balance")
        print("2.Deposit")
        print("3.Withdraw")
        print("4.Exit")

        choice = input("Enter your choice: ")
        if choice == "1":
            show_balance(balance)
        elif choice == "2":
            balance += deposit(balance)
        elif choice == "3":
            balance -= withdraw(balance)
        elif choice == "4":
            is_running = False
        else:
            print("Sorry, I didn't understand that. Please try again.")

    print("Thank You for using our Banking Program.")

if __name__ == "__main__":
    main()
    
import random

def spin_row():
    symbols = ('🍒', '🍉', '🍋', '🔔')
    results = []

    for i in range(3):
        results.append(random.choice(symbols))
    return results

def print_row(row):
    print(" | ".join(row))

def get_payout(row, bet):
    if row[0] == row[1] == row[2]:
        return bet * 10
    return 0

def main():
    balance = int(input("Enter your balance: "))
    first_balance = balance
    running = True

    if balance <= 0:
        print("Please enter balance greater that 0")

    print("\n*************************")
    print("Welcome to Python Slots")
    print("Symbols: 🍒 🍉 🍋 🔔 ⭐")
    print("*************************\n")

    while running:
        print(f"Current Balance: ${balance:.2f}")

        bet = input(f"Enter your bet 'q' to quit: ")

        if bet == "q":
            if balance > first_balance:
                print(f"\nCongrats You Won ${balance - first_balance:.2f}!")
                print("Thank You for playing.")
                break
            print("Thank You for playing.")
            break

        if not bet.isdigit():
            print("Please enter a valid number.")
            continue

        bet = int(bet)

        if bet > balance:
            print("You don't have enough money.")
            continue

        if bet < 0:
            print("Amount must be greater than 0.")
            continue


        row = spin_row()
        print("Spinning...\n")
        print_row(row)

        payout = get_payout(row, bet)

        if payout > 0:
            print(f"\nYou Won ${payout:.2f}!")
            balance += payout

        else:
            balance -= bet
            print(f"\nSorry you lost this round")

        if balance <= 0:
            print(f"\nSorry you don't have enough money.")

            playagain = True
            while playagain:
                play_again = input(f"Do you want to play again? (yes/no): ").lower()

                if play_again == "yes":
                    amount = int(input(f"\nEnter your amount: "))
                    balance += amount
                    playagain = False
                    continue

                elif play_again == "no":
                    print(f"\nThank You for playing.")
                    playagain = False
                    running = False
                else :
                    print("Sorry, I didn't understand that. Please try again.")


if __name__ == '__main__':
    main()

class Car:
    def __init__(self, model, year, color, for_sale):
        self.model = model
        self.year = year
        self.color = color
        self.for_sale = for_sale

car1 = Car("Mustang", 2024, "red", False)
car2 = Car("Corvette", 2025, "blue", True)
car3 = Car("Charger", 2026, "yellow", True)

print(car2.model)
print(car2.year)
print(car2.color)


class Animal:
    def __init__(self, name):
        self.name = name
        
        self.is_alive = True

    def eat(self):
        print(f"{self.name} is eating.")

    def sleep(self):
        print(f"{self.name} is sleeping.")

class Dog(Animal):
    def speak(self):
        print(f"Woof")

class Cat(Animal):
    def speak(self):
        print(f"Meow")

dog = Dog("Scooby")
cat = Cat("Garfield")

print(dog.name)
dog.eat()
cat.sleep()
cat.speak()

class Shape:
    def __init__(self, color,is_filled):
        self.color = color
        self.is_filled = is_filled

    def describe(self):
        print(f"it is a {self.color} and {'filled' if self.is_filled else 'not filled'}.")

class Circle(Shape):
    def __init__(self, color, is_filled, radius):
        super().__init__(color, is_filled)
        self.radius = radius

    def describe(self):
        print(f"It is a circle with an area of {3.14 * self.radius * self.radius}cm^2.")
        super().describe()

class Square(Shape):
    def __init__(self, color, is_filled, width):
        super().__init__(color, is_filled)


circle = Circle("White", True, 5)
square = Square("Blue", False, 6)

circle.describe()

#Static Method
class Employee:
    def __init__(self, name, position):
        self.name = name
        self.position = position

    def get_info(self):
        return f"{self.name} = {self.position}"

    @staticmethod
    def is_valid_position (position):
        valid_positions = ["Manager", "Cashier", "Cook", "Janitor"]
        return position in valid_positions

employee1 = Employee ("Eugine", "Manager")
employee2 = Employee ("Squidward", "Cashier")
employee3 = Employee ("Spongebob", "Cook")

print(employee1.get_info())

#Class Method
class Student:

    count = 0
    total_gpa = 0

    def __init__(self, name, gpa):
        self.name = name
        self.gpa = gpa
        Student.count += 1
        Student.total_gpa += gpa

    #Instance Method
    def get_info(self):
        return f"{self.name} {self.gpa}"

    @classmethod
    def get_count(cls):
        return f"Total # of Students: {cls.count}"

    @classmethod
    def get_average_gpa(cls):
        if cls.count == 0:
            return 0
        else:
            return f"{cls.total_gpa / Student.count:.2f}"


student1 = Student("Spongebob", 3.2)
student2 = Student("Patrick", 2.0)
student3 = Student("Sandy", 4.0)

print(student1.get_info())
print(student2.get_info())
print(Student.get_average_gpa())

#Magic Methods
class Book:

    def __init__(self, title, author, num_pages):
        self.title = title
        self.author = author
        self.num_pages = num_pages

    def __str__(self):
        return f"Title: {self.title}, Author: {self.author} Pages: {self.num_pages}"

    def __eq__(self, other):
        return self.title == other.title and self.author == other.author

    def __lt__(self, other):
        return self.num_pages < other.num_pages

    def __gt__(self, other):
        return self.num_pages > other.num_pages

    def __add__(self, other):
        return self.num_pages + other.num_pages

    def __contains__(self, keyword):
        return keyword in self.title or keyword in self.author

    def __getitem__(self, key):
        if key == 'title':
            return self.title
        if key == 'author':
            return self.author


book1 = Book("The Hobbit", "J.R.R Tolkien", 310)
book2 = Book("Harry Potter and the Philosopher's Stone","J.K Rowling", 223)

print(book2["author"])

#@property
class Rectangle:
    def __init__(self, width, height):
        self._width = width
        self._height = height

    @property
    def width(self):
        return f"{self._width:.1f}cm"

    @property
    def height(self):
        return f"{self._height:.1f}cm"

    @width.setter
    def width(self, new_width):
        if new_width > 0:
            self._width = new_width
        else:
            print("Please enter a valid width.")

    @height.setter
    def height(self, new_height):
        if new_height > 0:
            self.height = new_height
        else:
            print("Please enter a valid height.")

    @width.deleter
    def width(self):
        del self._width
        print("Width deleted.")



rectangle = Rectangle(3, 4)

rectangle.width = 5

print(rectangle.width)
print(rectangle.height)

del rectangle.width

def add_sprinkles(func):
    def wrapper():
        print("Adding sprinkles...")
        func()
    return wrapper

@add_sprinkles
def get_ice_cream():
    print("Here is your ice cream!")

get_ice_cream()

#Threading
import threading
import time

def walk_dog(first):
    time.sleep(8)
    print("You finish walking the dog")

def take_out_trash():
    time.sleep(2)
    print("You take out the trash")

def get_mail():
    time.sleep(4)
    print("You get the mail")

chore1 = threading.Thread(target=walk_dog, args=("Scooby",))
chore1.start()

chore2 = threading.Thread(target=take_out_trash)
chore2.start()

chore3 = threading.Thread(target=get_mail)
chore3.start()

import requests

base_url = "https://pokeapi.co/api/v2/"

def get_pokemon_info(name):
    url = f"{base_url}/pokemon/{name}"
    response = requests.get(url)

    if response.status_code == 200:
        pokemon_data = response.json()
        return pokemon_data
    else:
        print(f"failed to retrieve data")

pokemon_name = "eevee"
pokemon_info = get_pokemon_info(pokemon_name)

if pokemon_info:
    print(f"{pokemon_info["name"]}")
    print(f"{pokemon_info["id"]}")
    print(f"{pokemon_info["height"]}")
    print(f"{pokemon_info["weight"]}")

#PyQty5
import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QRadioButton
from PyQt5.QtGui import QIcon
from PyQt5.QtGui import QFont
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPixmap

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("My first GUI")
        self.setGeometry(600, 300, 600, 400)
        self.radio1 = QRadioButton("Visa", self)
        self.radio2 = QRadioButton("Mastercard", self)
        self.radio3 = QRadioButton("Gift card", self)
        self.radio4 = QRadioButton("In-Store", self)
        self.radio5 = QRadioButton("Online", self)


    def initUI(self):
        self.radio1.setGeometry(0, 0)

if __name__ == '__main__':
    main()

import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QRadioButton, QWidget, QVBoxLayout
from PyQt5.QtGui import QIcon
from PyQt5.QtGui import QFont
from PyQt5.QtCore import QTimer, QTime, Qt
from PyQt5.QtGui import QPixmap

class DigitalClock(QWidget):
    def __init__(self):
        super().__init__()
        self.time_label = QLabel(self)
        self.timer = QTimer(self)
        self.initUI()

    def initUI(self):
        self.setWindowTitle("Digital Clock")
        self.setGeometry(600, 400, 300, 100)

        vbox = QVBoxLayout()
        vbox.addWidget(self.time_label)
        self.setLayout(vbox)

        self.time_label.setAlignment(Qt.AlignCenter)

        self.time_label.setStyleSheet("font-size: 150px;"
                                      "font-family: Arial;"
                                      "color: hsl(111, 100%, 50%);"
                                      )
        self.setStyleSheet("background-color: black;")

        self.timer.timeout.connect(self.update_time)
        self.timer.start(1000)

        self.update_time()

    
    def update_time(self):
        current_time = QTime.currentTime().toString("hh:mm:ss AP")
        self.time_label.setText(current_time)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    clock = DigitalClock()
    clock.show()
    sys.exit(app.exec_())
''' #------------

import sys
from PyQt5.QtWidgets import (QApplication, QLabel,
                             QWidget, QVBoxLayout, QPushButton, QHBoxLayout)
from PyQt5.QtCore import QTimer, QTime, Qt

class Stopwatch(QWidget):
    def __init__(self):
        super().__init__()
        self.time = QTime(0, 0, 0, 0)
        self.time_label= QLabel("00:00:00", self)
        self.start_button = QPushButton("Start", self)
        self.stop_button = QPushButton("Stop", self)
        self.reset_button = QPushButton("Reset", self)
        self.timer = QTimer(self)
        self.initUI()

    def initUI(self):
        self.setWindowTitle("Stopwatch")

        vbox = QVBoxLayout()
        vbox.addWidget(self.time_label)

        self.setLayout(vbox)
        self.time_label.setAlignment(Qt.AlignCenter)

        hbox = QHBoxLayout()

        hbox.addWidget(self.start_button)
        hbox.addWidget(self.stop_button)
        hbox.addWidget(self.reset_button)

        vbox.addLayout(hbox)

        self.setStyleSheet("""
            QPushButton, QLabel{
                padding: 20px;
                font-weight: bold;
                font-family: calibri;
            }
        
            QPushButton {
                font-size: 50px;
            }
            QLabel {
                font-size: 120px;
                background-color: hsl(200, 100%, 85%);
                border-radius: 20px;
            }
        """)

        self.start_button.clicked.connect(self.start)
        self.stop_button.clicked.connect(self.stop)
        self.reset_button.clicked.connect(self.reset)
        self.timer.timeout.connect(self.update_display)


    def start(self):
        self.timer.start(10)

    def stop(self):
        self.timer.stop()

    def reset(self):
        self.timer.stop()
        self.time = QTime(0, 0, 0, 0)
        self.time_label.setText(self.format_time(self.time))

    def format_time(self, time):
        hours = time.hour()
        minutes = time.minute()
        seconds = time.second()
        milliseconds = time.msec() // 10
        return f"{hours:02}:{minutes:02}:{seconds:02}:{milliseconds:02}"

    def update_display(self):
        self.time = self.time.addMSecs(10)
        self.time_label.setText(self.format_time(self.time))

if __name__ == '__main__':
    app = QApplication(sys.argv)
    stopwatch = Stopwatch()
    stopwatch.show()
    sys.exit(app.exec_())








