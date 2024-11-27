#!/usr/bin/env python3

def admin_login(username, password):
    return (
        "Access granted" 
        if (username == "admin" or username == "ADMIN") and password == "12345" 
        else "Access denied"
    )

def hows_the_weather(temperature):
    return (
        "It's brisk out there!" if temperature < 40
        else "It's a little chilly out there!" if 40 <= temperature <= 65
        else "It's too dang hot out there!" if temperature > 85
        else "It's perfect out there!"
    )

def fizzbuzz(num):
    return (
        "FizzBuzz" if num % 3 == 0 and num % 5 == 0
        else "Fizz" if num % 3 == 0
        else "Buzz" if num % 5 == 0
        else num
    )

def calculator(operation, num1, num2):
    return (
        num1 + num2 if operation == "+"
        else num1 - num2 if operation == "-"
        else num1 * num2 if operation == "*"
        else num1 / num2 if operation == "/" and num2 != 0
        else "Division by zero is undefined" if operation == "/" and num2 == 0
        else (print("Invalid operation!") or None)
    )
