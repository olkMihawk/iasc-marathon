# Завданя 1 – Телефонна книга
contacts = {
    "Anna": "093-123-45-67",
    "Ivan": "050-888-99-00",
    "Olha": "097-777-33-22"
}
contacts["Taras"] = "063-000-11-22"
del contacts["Ivan"]
for name, number in contacts.items():
    print("Ім'я:", name)
    print("Номер:", number)
    print("---")
if "Katya" in contacts:
    print("Контакт Katya є в списку")
else:
    print("Контакту Katya нема")
# Завданя 2 – Оцінки по предметах
grades = {
    "math": 88,
    "physics": 75,
    "english": 93,
    "history": 59
}
max_subject = max(grades, key=grades.get)
print("Предмет з найвищим балом:",max_subject)
average = sum(grades.values()) / len(grades)
print("Середній бал:", average)
high_scores = [subject for subject, score in grades.items() if score > 80]
print("Предмети з оцінкою понад 80:", high_scores)
# Завдання 3 – Рахунок клієнтів
transactions = [
    ("Anna", 200),
    ("Ivan", -50),
    ("Anna", 100),
    ("Olha", 500),
    ("Ivan", 150),
    ("Olha", -100),
]
balances = {}
for name, amount in transactions:
    balances[name] = balances.get(name, 0) + amount

print("Баланси клієнтів:", balances)

richest = max(balances, key=balances.get)
print("Клієнт з найбільшим балансом:", richest)

negatives = [name for name, balance in balances.items() if balance < 0]
print("Клієнти з від’ємним балансом:", negatives)

# Завдання 4 – Підрахунок слів
text = "hello world hello again hello world test world"
words = text.split()

# Підрахунок слів
word_count = {}
for word in words:
    word_count[word] = word_count.get(word, 0) + 1

print("Кількість слів:", word_count)

# Завдання 5 – JSON: словник у рядок
import json

student = {
    "name": "Anna",
    "age": 20,
    "courses": ["math", "physics", "english"]
}

student_json = json.dumps(student)
print("JSON-рядок:", student_json)

student_dict = json.loads(student_json)

student_dict["courses"].append("history")

print("Оновлений словник студента:", student_dict)