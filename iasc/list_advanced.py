# Умова (Завдання 1)
students = ["Anna", "Ivan", "Olha", "Taras", "Katya"]
grades = [95, 62, 47, 88, 53]

# Ім'я студента мз найвищим балом
max_index = grades.index(max(grades))
print("Студент з найвищим балом", students[max_index])

# Студенти з оцінкою більше 60
passed_students = [students[i] for i in range(len(grades)) if grades[i] > 60]
print("Студенти з оцінкою більше 60:", passed_students)

# Кількість студентів, які не склали
failed_count = sum(1 for grade in grades if grade < 60)
print("Кількість студентів, які не склали:", failed_count)

# Умова (Завдання 2)
logs = ["ok", "error", "fail", "ok", "error", "warning", "ok", "fail"]

# Порахуй, скільки кожного типу повідомлень
unique_logs = set(logs)
for log_type in unique_logs:
    print(f"{log_type}: {logs.count(log_type)}")
    
# Виведи відсоток повідомлень зі словом error
error_count = logs.count("error")
percent_error = (error_count / len(logs)) * 100
print(f"Відсоток повідомлень 'error': {percent_error:.2f}%")

# Умова (Завдання 3)
expenses = [
    ["Понеділок", 120],
    ["Вівторок", 80],
    ["Середа", 150],
    ["Четвер", 0],
    ["П’ятниця", 250],
    ["Субота", 300],
    ["Неділя", 200]
]

# День з найбільшими витратами
max_expense = max(expenses, key=lambda x: x[1])
print("Найбільші витрати були у:", max_expense[0])

# Загальні витрати за тиждень
total = sum(day[1] for day in expenses)
print("Загальні витрати за тиждень:", total, "грн")

# Дні, коли витрати були більше 100
high_spending_days = [day[0] for day in expenses if day[1] > 100]
print("Дні з витратами більше 100 грн:", high_spending_days)

# Завдання 4 - Робота з вкладеними списками
products = [
    ["яблуко", 2, 12.5],
    ["банан", 5, 8.0],
    ["молоко", 1, 34.0],
    ["хліб", 2, 16.0]
]

# Загальна сума чеку
total_sum = sum(item[1] * item[2] for item in products)
print("Загальна сума чеку:", total_sum, "грн")

# Найдорожчий товар за одиницю
most_expensive = max(products, key=lambda x: x[2])
print("Найдорожчий товар за одиницю:", most_expensive[0])

# Новий список: "товар - сума грн"
receipt_lines = [f"{item[0]} - {item[1] * item[2]} грн" for item in products]
print("Чек:")
for line in receipt_lines:
    print(line)

# Завдання 5 - Генератор квадратів з умовою
squares = [x**2 for x in range(1, 30) if x % 2 == 0 and x % 4 != 0 and x not in [10, 14, 18]]
print("Список квадратів з умовою:", squares)
