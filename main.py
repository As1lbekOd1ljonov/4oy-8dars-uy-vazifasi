# vazifa 1
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

kvadrat_list = []
def kvadrat(number):
    res = number ** 2
    return res

a = map(kvadrat, numbers)
l = list(a)
print(l)

# ==========================================================

# vazifa 2
l = ["A", "a", "B", "b", "C", "c", "D", "d"]
def isupper(text: str):
    if text.isupper():
        return text

a = filter(isupper, l)
print(list(a))

# ==========================================================

# vazifa 3
phone_numbers = ["+998991234567", "+79454874459", "+14385001031"]
def mamlakat(phone_number: str):
    if phone_number.startswith("+998"):
        return f"{phone_number} bu O'zbekistonga tegishli nomer!"
    elif phone_number.startswith("+79"):
        return f"{phone_number} bu Rossiyaga tegishli nomer!"
    elif phone_number.startswith("+1"):
        return f"{phone_number} bu Amerikaga tegishli nomer!"
    return

a = map(mamlakat, phone_numbers)
s = list(a)
print(s)

# ==========================================================

# vazifa 4
names = ['alfred', 'tabitha', 'william', 'arla']
def capitalize(string: str):
    return string.capitalize()

title = map(capitalize, names)
print(list(title))

# ==========================================================

# vazifa 5
scores = [66, 90, 68, 59, 76, 60, 88, 74, 81, 65]
def ketta_son(number: int):
    if number > 75:
        return number


a = filter(ketta_son, scores)
b = list(a)
print(b)

# ==========================================================

# vazifa 6
words = ['Anna', 'Alexey', 'Alla', 'Kazak', 'Dom']
palindromes = list(filter(lambda word: word.lower() == word.lower()[::-1], words))
print(palindromes)

# ==========================================================

# vazifa 7
meva = ['apple', 'banana', 'cherry']
def len_text(text):
    return len(text)
a = map(len_text, meva)
print(list(a))

# ==========================================================

# vazifa 8
a = ['apple', 'banana', 'cherry']
b = ['orange', 'lemon', 'pineapple']
def qoshish(a, b):
    return a + b

s = map(qoshish, a, b)
print(list(s))

# ==========================================================

# vazifa 9
names1 = ['Anna', 'Alexey', 'Alla', 'Kazak', 'Dom']
names2 = ["Sobir", "Bakir", "Jalil", "Toxir"]

new_names = []
def names(names1, names2):
    return new_names.append(names1 + names2)

a = map(names, names1, names2)
b = list(a)
print(new_names)

# ==========================================================

# vazifa 10
def count_occurrences_map(lst, element):
    return sum(map(lambda x: x == element, lst))
example_list = ['apple', 'banana', 'apple', 'orange', 'banana', 'apple']
example_element = 'apple'
print(count_occurrences_map(example_list, example_element))

# ==========================================================

# vazifa 11
I1 = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
I2 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
common_elements = list(filter(lambda x: x in I2, I1))

print(common_elements)

# ==========================================================

# vazifa 12
programming_languages = ['Python', 'C', 'C++', 'C#', 'Java', 'Basic', 'Kotlin', 'Pascal', 'JavaScript', 'Go', 'Dart', 'Assambler', 'Ruby', 'Rust', 'Mojo', 'Swift', 'Php']
odd_indexed_languages = list(map(lambda x: programming_languages[x], filter(lambda i: i % 2 == 0, range(len(programming_languages)))))

print(odd_indexed_languages)

# ==========================================================

# vazifa 13
programming_languages = ['Python', 'C', 'C++', 'C#', 'Java', 'Basic', 'Kotlin', 'Pascal', 'JavaScript', 'Go', 'Dart', 'Assambler', 'Ruby', 'Rust', 'Mojo', 'Swift', 'Php']

start_index = programming_languages.index('Basic')
elements_from_basic = list(map(lambda x: programming_languages[x], range(start_index, len(programming_languages))))

print(elements_from_basic)

# ==========================================================

# vazifa 14
from collections import namedtuple

Student = namedtuple('Student', ['name', 'group', 'average_grade'])

students = [
    Student(name='Toxir', group='101', average_grade=88.5),
    Student(name='Bakir', group='102', average_grade=92.0),
    Student(name='Sobir', group='103', average_grade=85.7),
]

yuqori_bal = max(students, key=lambda student: student.average_grade)

print(f"Eng yuqori bahoga ega talaba: {yuqori_bal.name}, Guruh: {yuqori_bal.group}, O'rtacha baho: {yuqori_bal.average_grade}")

# ==========================================================

# vazifa 15
def kvadrat_generator():
    for son in range(1, 20 + 1):
        yield son ** 2

for kvadrat in kvadrat_generator():
    print(kvadrat)

# ==========================================================

# vazifa 16
def matn_uzunligi_olchash(matn):

    def uzunlik():
        return len(matn)
    return uzunlik

matn = input("Matn kiritin: ")
uzunlikni_olchash = matn_uzunligi_olchash(matn)
print(f"Matn uzunligi: {uzunlikni_olchash()}")

# ==========================================================

# vazifa 17
def salomlashish_yarat(ism):

    def salom():
        return f"Salom, {ism}!"
    return salom

ism = input("Ism kiritin: ").capitalize()
salomlashish = salomlashish_yarat(ism)
print(salomlashish())