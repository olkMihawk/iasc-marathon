# 1. Функція, що виводить привітання
def hello_world():
    print("Hello, world!")
# 2. Функція, що вітає користувача за ім’ям
def greet(name):
    print(f"Привіт, {name}!")
# 3. Функція, що повертає квадрат числа
def square(n):
    return n ** 2
# 4. Функція, що повертає суму двох чисел
def add(a, b):
    return a + b
# 5. Функція з параметром за замовчуванням
def greet(name="Гість"):
    print(f"Привіт, {name}!")
# 6. Функція факторіалу (n!)
def factorial(n):
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result
# 7. Перевірка на парність
def is_even(n):
    return n % 2 == 0
# 8. Виведення чисел від 1 до n
def print_numbers(n):
    for i in range(1, n + 1):
        print(i)
# 9. Пошук імені у списку
def find_name(name, name_list):
    return name in name_list
# 10. Повертає найбільше з трьох чисел
def max_of_three(a, b, c):
    return max(a, b, c)
# 11. Повертає рядок навпаки
def reverse_string(s):
    return s[::-1]
# 12. Рахує кількість голосних у рядку
def count_vowels(s):
    vowels = "аеєиіїоуюяAEIOUYaeiouy"
    return sum(1 for char in s if char in vowels)
# 13. Середнє значення з довільної кількості чисел
def average(*numbers):
    if not numbers:
        return 0
    return sum(numbers) / len(numbers)
# 14. Виводить інформацію про користувача
def print_user_info(**info):
    for key, value in info.items():
        print(f"{key}: {value}")
# 15. Вкладена функція
def outer():
    def inner():
        print("Я - вкладена функція!")
    inner()
    