# Q4:

def is_palindrome(number):
    """Checks if a given number (as string) is a palindrome."""
    return number == number[::-1]

numbers = [
    "9847255590886266818998186626880955527489",
    "6800923757255865070000705685527573290086",
    "6892149109325320763773670235239019412986",
    "1414884937242655719669145562427394884141"
]

for num in numbers:
    result = "is a palindrome" if is_palindrome(num) else "is NOT a palindrome"
    print(f"{num} {result}")
