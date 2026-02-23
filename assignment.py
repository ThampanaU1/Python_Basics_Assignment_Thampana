import random
import math
from datetime import datetime

# ==========================================================
# PYTHON BASICS ASSIGNMENT
# Name: Thampana u
# Total Questions: 20
# ==========================================================


# ----------------------------------------------------------
# QUESTION 1: Personal Bio Card
# ----------------------------------------------------------
def question1():
    
     # Using variables for each field 
    name = "Thampana u"
    age = 21
    course = "Python Programming"
    college = "SJBIT"
    email = "thampana26@example.com"

     # Printing formatted output
    print("╔════════════════════════════════╗")
    print("║       STUDENT BIO CARD         ║")
    print("╠════════════════════════════════╣")
    print(f"║ Name    : {name:<18}   ║")
    print(f"║ Age     : {age} years{'':<10}   ║")
    print(f"║ Course  : {course:<18}   ║")
    print(f"║ College : {college:<18}   ║")
    print(f"║ Email   : {email:<18}  ║")
    print("╚════════════════════════════════╝")
    # Calling the function so it executes



# ----------------------------------------------------------
# QUESTION 2: Simple Calculator
# ----------------------------------------------------------
def question2():
    try:
        # Asking user for two numbers
        a = float(input("Enter first number: "))
        b = float(input("Enter second number: "))

        print(f"{a} + {b} = {a+b}")
        print(f"{a} - {b} = {a-b}")
        print(f"{a} * {b} = {a*b}")

        if b != 0:
            print(f"{a} / {b} = {a/b:.2f}")
            print(f"{a} % {b} = {a%b}")
        else:
            print("Division and modulus not possible (division by zero)")

        print(f"{a} ^ {b} = {a**b}")
# Handling division safely
    except:
        print("Invalid input")


# ----------------------------------------------------------
# QUESTION 3: String Manipulator
# ----------------------------------------------------------


def question3():
    try:
        # Step 1: Ask the user to enter a sentence
        user_sentence = input("Enter a sentence: ")

        # Step 2: Check if the user entered empty input
        if user_sentence.strip() == "":
            print("You entered an empty sentence.")
            return

        # Step 3: Calculate total characters (including spaces)
        characters_with_spaces = len(user_sentence)

        # Step 4: Calculate total characters (excluding spaces)
        characters_without_spaces = len(user_sentence.replace(" ", ""))

        # Step 5: Split sentence into words
        words_list = user_sentence.split()

        # Step 6: Count total words
        total_words = len(words_list)

        # Step 7: Get first and last word safely
        first_word = words_list[0]
        last_word = words_list[-1]

        # Step 8: Reverse the entire sentence
        reversed_sentence = user_sentence[::-1]

        # Step 9: Display all required outputs
        print("\nOriginal:", user_sentence)
        print("Characters (with spaces):", characters_with_spaces)
        print("Characters (without spaces):", characters_without_spaces)
        print("Words:", total_words)
        print("UPPERCASE:", user_sentence.upper())
        print("lowercase:", user_sentence.lower())
        print("Title Case:", user_sentence.title())
        print("First word:", first_word)
        print("Last word:", last_word)
        print("Reversed:", reversed_sentence)

    except Exception as error:
        # Step 10: Handle unexpected errors
        print("An error occurred:", error)





# ----------------------------------------------------------
# QUESTION 4: Age Calculator
# ----------------------------------------------------------
from datetime import datetime
def question4():
    try:
        current_year = datetime.now().year
        birth_year = int(input("Enter birth year: "))

        if birth_year > current_year:
            print("Birth year cannot be in the future.")
            return

        age = current_year - birth_year

        print("Current Age:", age)
        print("Age in Months:", age * 12)
        print("Age in Days (approx):", age * 365)
        print("Age in Hours:", age * 365 * 24)
        print("Age in Minutes:", age * 365 * 24 * 60)
        print("Years until 100:", 100 - age)

    except:
        print("Invalid input. Please enter a valid year.")

# ----------------------------------------------------------
# QUESTION 5: Bill Splitter
# ----------------------------------------------------------
def question5():
    try:
        bill = float(input("Enter total bill: "))
        people = int(input("Number of people: "))
        tax_percent = float(input("Tax percentage: "))
        tip_percent = float(input("Tip percentage: "))

        # Handling invalid people count
        if people <= 0:
            print("Number of people must be greater than zero.")
            return

        tax = bill * tax_percent / 100
        after_tax = bill + tax

        tip = after_tax * tip_percent / 100
        total = after_tax + tip

        per_person = total / people

        print("\n=== BILL BREAKDOWN ===")
        print("Subtotal:", bill)
        print("Tax:", tax)
        print("After tax:", after_tax)
        print("Tip:", tip)
        print("Total:", total)
        print("Per person:", per_person)

    except:
        print("Invalid input")


# ----------------------------------------------------------
# QUESTION 6: Grade Calculator
# ----------------------------------------------------------
def question6():
    marks_list = []

    # Taking marks for 5 subjects with error handling
    for subject_number in range(1, 6):
        try:
            mark = float(input(f"Enter marks for subject {subject_number} (0–100): "))
            if mark < 0 or mark > 100:
                print("Marks must be between 0 and 100.")
                return
            marks_list.append(mark)
        except ValueError:
            print("Invalid input! Please enter a number.")
            return

    # Calculating basic results
    total_marks = sum(marks_list)
    percentage = (total_marks / 500) * 100
    passed_all = all(mark >= 40 for mark in marks_list)

    # Determining grade
    if percentage >= 90:
        grade = "A+ (Outstanding)"
    elif percentage >= 80:
        grade = "A (Excellent)"
    elif percentage >= 70:
        grade = "B (Good)"
    elif percentage >= 60:
        grade = "C (Average)"
    elif percentage >= 50:
        grade = "D (Pass)"
    else:
        grade = "F (Fail)"

    # Displaying final results
    print("Marks:", marks_list)
    print(f"Total Marks: {total_marks}/500")
    print(f"Percentage: {percentage:.2f}%")
    print("Grade:", grade)
    print("Result:", "Pass" if passed_all else "Fail")


# ----------------------------------------------------------
# QUESTION 7: Temperature Converter
# ----------------------------------------------------------
def question7():
    while True:
        print("\n===== TEMPERATURE CONVERTER =====")
        print("1. Celsius to Fahrenheit")
        print("2. Fahrenheit to Celsius")
        print("3. Celsius to Kelvin")
        print("4. Kelvin to Celsius")
        print("5. Fahrenheit to Kelvin")
        print("6. Kelvin to Fahrenheit")
        print("7. Exit")

        try:
            user_choice = int(input("Enter choice: "))
        except ValueError:
            print("Invalid input! Enter a number 1–7.")
            continue

        if user_choice == 7:
            print("Exiting converter...")
            break

        try:
            temperature_value = float(input("Enter temperature value: "))
        except ValueError:
            print("Invalid temperature entered!")
            continue

        # Performing conversions based on menu choice
        if user_choice == 1:
            print("Result:", (temperature_value * 9/5) + 32, "°F")
        elif user_choice == 2:
            print("Result:", (temperature_value - 32) * 5/9, "°C")
        elif user_choice == 3:
            print("Result:", temperature_value + 273.15, "K")
        elif user_choice == 4:
            print("Result:", temperature_value - 273.15, "°C")
        elif user_choice == 5:
            print("Result:", (temperature_value - 32) * 5/9 + 273.15, "K")
        elif user_choice == 6:
            print("Result:", (temperature_value - 273.15) * 9/5 + 32, "°F")
        else:
            print("Invalid choice! Please pick between 1 and 7.")



# ----------------------------------------------------------
# QUESTION 8: Leap Year Checker
# ----------------------------------------------------------
def question8():
    try:
        year = int(input("Enter a year: "))
    except ValueError:
        print("Invalid input! Enter a valid year.")
        return

    # Applying leap year rules
    if year % 4 != 0:
        print(year, "is NOT a leap year — not divisible by 4.")
    elif year % 100 != 0:
        print(year, "IS a leap year — divisible by 4 but not by 100.")
    elif year % 400 == 0:
        print(year, "IS a leap year — divisible by 400.")
    else:
        print(year, "is NOT a leap year — divisible by 100 but not by 400.")

# ----------------------------------------------------------
# QUESTION 9: Ticket Pricing System
# ----------------------------------------------------------
def question9():
    try:
        age = int(input("Enter age: "))
        day = input("Enter day of the week: ").strip().lower()
        number_of_tickets = int(input("Number of tickets: "))
    except ValueError:
        print("Invalid input! Provide correct values.")
        return

    if age < 3:
        base_price = 0
    elif age <= 12:
        base_price = 150
    elif age <= 59:
        base_price = 300
    else:
        base_price = 200

    # Weekend discount check
    if day in ["friday", "saturday", "sunday"]:
        discount = base_price * 0.20
    else:
        discount = 0

    price_after_discount = base_price - discount
    total_cost = price_after_discount * number_of_tickets

    print("Base price:", base_price)
    print("Discount applied:", discount)
    print("Price after discount:", price_after_discount)
    print("Total amount:", total_cost)
# ----------------------------------------------------------
# QUESTION 10: ATM Simulator
# ----------------------------------------------------------
def question10():
    account_balance = 10000  # initial balance

    while True:
        print("\n===== ATM SIMULATOR =====")
        print("1. Check Balance")
        print("2. Deposit Money")
        print("3. Withdraw Money")
        print("4. Exit")

        try:
            menu_choice = int(input("Enter choice: "))
        except ValueError:
            print("Invalid input. Enter 1–4.")
            continue

        # Option 1: Check balance
        if menu_choice == 1:
            print("Current Balance: ₹", account_balance)

        # Option 2: Deposit
        elif menu_choice == 2:
            try:
                deposit_amount = float(input("Enter amount to deposit: "))
            except ValueError:
                print("Invalid amount!")
                continue

            if deposit_amount <= 0:
                print("Amount must be positive.")
                continue

            account_balance += deposit_amount
            print("Deposit successful!")
            print("New Balance: ₹", account_balance)

        # Option 3: Withdraw
        elif menu_choice == 3:
            try:
                withdraw_amount = float(input("Enter amount to withdraw: "))
            except ValueError:
                print("Invalid amount!")
                continue

            if withdraw_amount <= 0:
                print("Amount must be positive.")
                continue

            if withdraw_amount > account_balance - 500:
                print("Insufficient balance! Minimum ₹500 required.")
                continue

            account_balance -= withdraw_amount
            print("Withdrawal successful!")
            print("New Balance: ₹", account_balance)

        # Option 4: Exit
        elif menu_choice == 4:
            print("Thank you! Exiting ATM.")
            break

        else:
            print("Invalid choice! Choose between 1–4.")



# ----------------------------------------------------------
# QUESTION 11: Pattern Printer
# ----------------------------------------------------------
def question11():
    print("\n=== NUMBER PATTERN PRINTER ===")
    print("1. Pattern 1")
    print("2. Pattern 2")
    print("3. Pattern 3")
    print("4. Pattern 4")

    try:
        pattern_choice = int(input("Choose a pattern (1-4): "))
        height = int(input("Enter height: "))
    except ValueError:
        print("Invalid input! Enter numbers only.")
        return

    print("\n=== OUTPUT ===")

    # Pattern 1
    if pattern_choice == 1:
        for row in range(1, height + 1):
            for num in range(1, row + 1):
                print(num, end=" ")
            print()

    # Pattern 2
    elif pattern_choice == 2:
        for row in range(1, height + 1):
            for _ in range(row):
                print(row, end=" ")
            print()

    # Pattern 3
    elif pattern_choice == 3:
        for row in range(height, 0, -1):
            for num in range(row, 0, -1):
                print(num, end=" ")
            print()

    # Pattern 4
    elif pattern_choice == 4:
        for row in range(1, height + 1):
            for num in range(1, row + 1):
                print(num, end="")
            for num in range(row - 1, 0, -1):
                print(num, end="")
            print()

    else:
        print("Invalid pattern choice!")


# ----------------------------------------------------------
# QUESTION 12: Multiplication Table
# ----------------------------------------------------------
def question12():
    try:
        base_number = int(input("Enter number: "))
        end_range = int(input("Enter range (end): "))
    except ValueError:
        print("Invalid input! Enter numbers only.")
        return

    print(f"\nMultiplication Table of {base_number}")
    for multiplier in range(1, end_range + 1):
        print(f"{base_number} x {multiplier} = {base_number * multiplier}")



# ----------------------------------------------------------
# QUESTION 13: Sum and Average Calculator
# ----------------------------------------------------------
def question13():

    try:
        total_count = int(input("How many numbers? "))
    except ValueError:
        print("Invalid input!")
        return

    if total_count <= 0:
        print("Count must be greater than 0.")
        return

    numbers = []

    # Collect numbers
    for i in range(1, total_count + 1):
        try:
            value = float(input(f"Enter number {i}: "))
            numbers.append(value)
        except ValueError:
            print("Invalid number!")
            return

    # Basic calculations
    total_sum = sum(numbers)
    average = total_sum / total_count
    maximum_value = max(numbers)
    minimum_value = min(numbers)

    sorted_numbers = sorted(numbers)
    mid = total_count // 2

    if total_count % 2 == 1:
        median_value = sorted_numbers[mid]
    else:
        median_value = (sorted_numbers[mid - 1] + sorted_numbers[mid]) / 2

    frequency = {}
    for num in numbers:
        frequency[num] = frequency.get(num, 0) + 1

    highest_frequency = max(frequency.values())
    mode_values = [num for num, count in frequency.items() if count == highest_frequency]

    print("\n=== STATISTICS ===")
    print("Numbers:", numbers)
    print("Sum:", total_sum)
    print("Average:", average)
    print("Maximum:", maximum_value)
    print("Minimum:", minimum_value)
    print("Median:", median_value)

    if len(mode_values) == len(numbers):
        print("Mode: No mode (all numbers are unique)")
    else:
        print("Mode:", mode_values)


# ----------------------------------------------------------
# QUESTION 14: Factorial Calculator
# ----------------------------------------------------------
def question14():
    try:
        number = int(input("Enter a number: "))
    except ValueError:
        print("Invalid input!")
        return

    if number < 0:
        print("Factorial of negative numbers is not defined.")
        return

    # Calculating factorial step-by-step
    factorial_value = 1
    steps = ""

    for i in range(number, 0, -1):
        factorial_value *= i
        steps += f"{i} × " if i > 1 else f"{i}"

    print(f"{number}! = {steps} = {factorial_value}")



# ----------------------------------------------------------
# QUESTION 15: Prime Number Checker
# ----------------------------------------------------------


def is_prime(num):
    # Handling edge cases
    if num < 2:
        return False
    if num == 2:
        return True

    # Checking divisibility
    for i in range(2, num):
        if num % i == 0:
            return False
    return True


def question15():
    # ---- PART 1: Single Number ----
    try:
        number = int(input("Enter a number: "))
    except ValueError:
        print("Invalid input!")
        return

    if is_prime(number):
        print(number, "is a PRIME number")
    else:
        print(number, "is NOT a prime number")

    # ---- PART 2: Range ----
    try:
        start_range = int(input("Enter start range: "))
        end_range = int(input("Enter end range: "))
    except ValueError:
        print("Invalid input!")
        return

    prime_list = []

    for n in range(start_range, end_range + 1):
        if is_prime(n):
            prime_list.append(n)

    print("Prime numbers in range:", prime_list)

# ----------------------------------------------------------
# QUESTION 16: Number Guessing Game
# ----------------------------------------------------------
# ----------------------------------------------------------
# QUESTION 16: Number Guessing Game
# ----------------------------------------------------------

def question16():
    best_score = None  # To track minimum number of attempts

    while True:
        print("\n=== NUMBER GUESSING GAME ===")
        print("Choose difficulty:")
        print("1. Easy   (1 - 50)")
        print("2. Medium (1 - 100)")
        print("3. Hard   (1 - 1000)")

        # Asking for difficulty with error handling
        try:
            difficulty_choice = int(input("Enter difficulty (1-3): "))
        except ValueError:
            print("Invalid input! Enter 1, 2, or 3.")
            continue

        # Setting difficulty range
        if difficulty_choice == 1:
            secret_number = random.randint(1, 50)
            max_range = 50
        elif difficulty_choice == 2:
            secret_number = random.randint(1, 100)
            max_range = 100
        elif difficulty_choice == 3:
            secret_number = random.randint(1, 1000)
            max_range = 1000
        else:
            print("Invalid choice! Choose 1, 2, or 3.")
            continue

        attempts_left = 7
        attempts_used = 0

        print(f"\nI have selected a number between 1 and {max_range}.")
        print("You have 7 attempts. Good luck!")

        # Guessing loop
        while attempts_left > 0:
            try:
                guess = int(input(f"\nEnter your guess (Attempts left {attempts_left}): "))
            except ValueError:
                print("Invalid input! Enter a valid number.")
                continue

            attempts_left -= 1
            attempts_used += 1

            if guess > secret_number:
                print("Too HIGH!")
            elif guess < secret_number:
                print("Too LOW!")
            else:
                print(f"\nCorrect! You guessed the number in {attempts_used} attempts.")

                if best_score is None or attempts_used < best_score:
                    best_score = attempts_used
                    print("NEW BEST SCORE!")
                break

            if abs(guess - secret_number) <= 5:
                print("Hint: You're very close!")

        if attempts_left == 0 and guess != secret_number:
            print("\nYou failed! The correct number was:", secret_number)

        play_again = input("\nDo you want to play again? (yes/no): ").strip().lower()
        if play_again != "yes":
            print("\nThanks for playing!")
            break

# ----------------------------------------------------------
# QUESTION 17: Palindrome Checker
# ----------------------------------------------------------
# ----------------------------------------------------------
# QUESTION 17: Palindrome Checker
# ----------------------------------------------------------
def question17():
    # Step 1: Take input from user
    user_input = input("Enter word/number: ")

    # Step 2: Store original and reversed values
    original_text = user_input
    reversed_text = user_input[::-1]

    # Step 3: Display original and reversed text
    print("Original:", original_text)
    print("Reversed:", reversed_text)

    # Step 4: Check palindrome (case-insensitive)
    if original_text.lower() == reversed_text.lower():
        print("Result: PALINDROME")
    else:
        print("Result: NOT a palindrome")

# ----------------------------------------------------------
# QUESTION 18: Calculator Using Functions
# ----------------------------------------------------------
# ----------------------------------------------------------
# QUESTION 18: Calculator Using Functions
# ----------------------------------------------------------

# Basic operation functions

def add(a, b):
    return a + b


def subtract(a, b):
    return a - b


def multiply(a, b):
    return a * b


def divide(a, b):
    try:
        return a / b
    except ZeroDivisionError:
        return "Error (division by zero)"


def modulus(a, b):
    return a % b


def power(a, b):
    return a ** b


def square_root(a):
    if a < 0:
        return "Error (square root of negative number)"
    return math.sqrt(a)


def percentage(a, b):
    # a% of b
    return (a / 100) * b


# Main calculator menu
def question18():

    while True:
        print("\n=== ADVANCED CALCULATOR MENU ===")
        print("1. Add")
        print("2. Subtract")
        print("3. Multiply")
        print("4. Divide")
        print("5. Modulus")
        print("6. Power")
        print("7. Square Root")
        print("8. Percentage")
        print("9. Exit")

        try:
            choice = int(input("Enter choice: "))
        except ValueError:
            print("Invalid input!")
            continue

        if choice == 9:
            print("Exiting calculator...")
            break

        # Two-number operations
        if choice in [1, 2, 3, 4, 5, 6, 8]:
            try:
                first_number = float(input("Enter first number: "))
                second_number = float(input("Enter second number: "))
            except ValueError:
                print("Invalid input!")
                continue

        # One-number operation
        if choice == 7:
            try:
                number = float(input("Enter number: "))
            except ValueError:
                print("Invalid input!")
                continue

        # Perform selected operation
        if choice == 1:
            print("Result:", add(first_number, second_number))
        elif choice == 2:
            print("Result:", subtract(first_number, second_number))
        elif choice == 3:
            print("Result:", multiply(first_number, second_number))
        elif choice == 4:
            print("Result:", divide(first_number, second_number))
        elif choice == 5:
            print("Result:", modulus(first_number, second_number))
        elif choice == 6:
            print("Result:", power(first_number, second_number))
        elif choice == 7:
            print("Result:", square_root(number))
        elif choice == 8:
            print(f"{first_number}% of {second_number} =", percentage(first_number, second_number))
        else:
            print("Invalid choice!")

# ----------------------------------------------------------
# QUESTION 19: Text Analysis Functions
# ----------------------------------------------------------

# Helper Functions

def count_words(text):
    return len(text.split())


def count_vowels(text):
    vowels = "aeiouAEIOU"
    return sum(1 for char in text if char in vowels)


def count_consonants(text):
    letters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
    vowels = "aeiouAEIOU"
    return sum(1 for char in text if char in letters and char not in vowels)


def reverse_text(text):
    return text[::-1]


def is_palindrome(text):
    cleaned = text.lower().replace(" ", "")
    return cleaned == cleaned[::-1]


def remove_vowels(text):
    vowels = "aeiouAEIOU"
    return "".join(char for char in text if char not in vowels)


def word_frequency(text):
    freq = {}
    for word in text.lower().split():
        freq[word] = freq.get(word, 0) + 1
    return freq


def longest_word(text):
    words = text.split()
    if not words:
        return ""
    return max(words, key=len)


def analyze_text(text):
    print("\n=== TEXT ANALYSIS ===")
    print("Words:", count_words(text))
    print("Vowels:", count_vowels(text))
    print("Consonants:", count_consonants(text))
    print("Reversed:", reverse_text(text))
    print("Palindrome:", "Yes" if is_palindrome(text) else "No")
    print("Without vowels:", remove_vowels(text))

    lw = longest_word(text)
    print(f"Longest word: {lw} ({len(lw)} letters)")

    freq = word_frequency(text)
    print("Word Frequency:")
    for word, count in freq.items():
        print(f"{word}: {count}")


# Main function called from menu
def question19():
    try:
        user_text = input("Enter text: ")
        if user_text.strip() == "":
            print("You entered empty text.")
            return
    except Exception:
        print("Invalid input!")
        return

    analyze_text(user_text)


# ----------------------------------------------------------
# QUESTION 20: Number System Functions
# ----------------------------------------------------------
# ----------------------------------------------------------
# QUESTION 20: Number System Functions
# ----------------------------------------------------------

def question20():

    # Factorial Function
    def factorial(n):
        if n < 0:
            return "Factorial not defined for negative numbers"
        result = 1
        for i in range(1, n + 1):
            result *= i
        return result

    # Prime Check
    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, n):
            if n % i == 0:
                return False
        return True

    # Fibonacci
    def fibonacci(n):
        if n <= 0:
            return "Invalid input"
        if n == 1:
            return 0
        if n == 2:
            return 1

        a, b = 0, 1
        for _ in range(n - 2):
            a, b = b, a + b
        return b

    # Sum of digits
    def sum_of_digits(n):
        return sum(int(d) for d in str(abs(n)))

    # Reverse number
    def reverse_number(n):
        sign = -1 if n < 0 else 1
        return sign * int(str(abs(n))[::-1])

    # Armstrong number check
    def is_armstrong(n):
        digits = str(n)
        power = len(digits)
        return sum(int(d) ** power for d in digits) == n

    # GCD
    def gcd(a, b):
        while b != 0:
            a, b = b, a % b
        return abs(a)

    # LCM
    def lcm(a, b):
        return abs(a * b) // gcd(a, b)

    # Perfect number check
    def is_perfect_number(n):
        if n <= 0:
            return False
        return sum(i for i in range(1, n) if n % i == 0) == n

    # Menu loop
    while True:
        print("\n=== NUMBER SYSTEM MENU ===")
        print("1. Factorial")
        print("2. Prime Check")
        print("3. Fibonacci Number")
        print("4. Sum of Digits")
        print("5. Reverse Number")
        print("6. Armstrong Check")
        print("7. GCD")
        print("8. LCM")
        print("9. Perfect Number Check")
        print("10. Exit")

        try:
            choice = int(input("Enter choice: "))
        except ValueError:
            print("Invalid input! Enter a number.")
            continue

        if choice == 10:
            print("Exiting Number System Menu...")
            break

        try:
            if choice in [1, 2, 3, 4, 5, 6, 9]:
                n = int(input("Enter a number: "))
            if choice in [7, 8]:
                a = int(input("Enter first number: "))
                b = int(input("Enter second number: "))
        except ValueError:
            print("Invalid input!")
            continue

        if choice == 1:
            print("Factorial:", factorial(n))
        elif choice == 2:
            print("Prime:", "Yes" if is_prime(n) else "No")
        elif choice == 3:
            print("Fibonacci:", fibonacci(n))
        elif choice == 4:
            print("Sum of digits:", sum_of_digits(n))
        elif choice == 5:
            print("Reversed number:", reverse_number(n))
        elif choice == 6:
            print("Armstrong:", "Yes" if is_armstrong(n) else "No")
        elif choice == 7:
            print("GCD:", gcd(a, b))
        elif choice == 8:
            print("LCM:", lcm(a, b))
        elif choice == 9:
            print("Perfect Number:", "Yes" if is_perfect_number(n) else "No")
        else:
            print("Invalid choice.")


# ==========================================================
# MAIN MENU
# ==========================================================
def main():
    while True:
        print("\n===== PYTHON BASICS ASSIGNMENT =====")
        print("1 - Question 1")
        print("2 - Question 2")
        print("3 - Question 3")
        print("4 - Question 4")
        print("5 - Question 5")
        print("6 - Question 6")
        print("7 - Question 7")
        print("8 - Question 8")
        print("9 - Question 9")
        print("10 - Question 10")
        print("11 - Question 11")
        print("12 - Question 12")
        print("13 - Question 13")
        print("14 - Question 14")
        print("15 - Question 15")
        print("16 - Question 16")
        print("17 - Question 17")
        print("18 - Question 18")
        print("19 - Question 19")
        print("20 - Question 20")
        print("0 - Exit")

        user_choice = input("Enter question number: ")

        if user_choice == "1":
            question1()
        elif user_choice == "2":
            question2()
        elif user_choice == "3":
            question3()
        elif user_choice == "4":
            question4()
        elif user_choice == "5":
            question5()
        elif user_choice == "6":
            question6()
        elif user_choice == "7":
            question7()
        elif user_choice == "8":
            question8()
        elif user_choice == "9":
            question9()
        elif user_choice == "10":
            question10()
        elif user_choice == "11":
            question11()
        elif user_choice == "12":
            question12()
        elif user_choice == "13":
            question13()
        elif user_choice == "14":
            question14()
        elif user_choice == "15":
            question15()
        elif user_choice == "16":
            question16()
        elif user_choice == "17":
            question17()
        elif user_choice == "18":
            question18()
        elif user_choice == "19":
            question19()
        elif user_choice == "20":
            question20()
        elif user_choice == "0":
            print("Exiting program...")
            break
        else:
            print("Invalid choice. Please try again.")


# Run the program
main()