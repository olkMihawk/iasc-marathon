shopping_list = ["хліб", "молоко", "сосиски", "сир", "вино"]
print("До додавання:", shopping_list)
shopping_list.append("чай")
print("Після додавання:", shopping_list)

grades = [9, 10, 9, 11, 12]
average = sum(grades) / len(grades)
print("Середній бал:", average)

names = ["Олександр", "Андрій", "Богдан", "Ірина", "Максим"]
names.sort()
print("Імена в алфавітному порядку:", names)

cities = ["Київ", "Львів", "Одеса", "Суми", "Донецьк"]
cities[1] = "Тернопіль"
print("Перше місто:", cities[0])
print("Останнє місто:", cities[-1])

movies = ["Інтерстеллар", "Темний лицар", "Перший Месник", "Тенет", "F1"]
print("Довжина списку:", len(movies))
movies.remove("Тенет")
movies.sort()
print("Після видалення і сортування:", movies)
