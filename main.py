import random

iterator = 1 #отвечает за количество генерируемых уроков

def GetLesson(subjects):# случайная выборка из subjects
    subjects_weights = [subject['rang'] for subject in subjects] # перебор объекта по рангу трудности / можно поменять критерий на имя или id
    SelectSubject = random.choices(subjects, subjects_weights)[0] # рандомно выбирает по id
    print(SelectSubject)
def GetLessons(iterator): # получаем уроки с GetLesson
    while iterator <= 4:  # генерация расписания для одного
        lesson = GetLesson(subjects)
        iterator += 1
def GetRaspWeek(): # генерируем раписание по неделям
    for dayWeek in DaysWeek: # перебор дней недели
        print(dayWeek["name"]) # вывод дня недели
        GetLessons(iterator) # вывод 4 уроков



DaysWeek = [
    {
        "index": 1,
        "name": "Понедельник",
    },
    {
        "index": 2,
        "name": "Вторник",
    },
    {
        "index": 3,
        "name": "Среда",
    },
    {
        "index": 4,
        "name": "Четверг",
    },
    {
        "index": 5,
        "name": "Пятница",
    },
    {
        "index": 6,
        "name": "Суббота",
    }
]
subjects = [
    {
        "id": 1,
        "name": "Математика",
        "rang": 8,
    },
    {
        "id": 2,
        "name": "Русский",
        "rang": 7,
    },
    {
        "id": 3,
        "name": "Английский",
        "rang": 7,
    },
    {
        "id": 4,
        "name": "Природоведение",
        "rang": 6,
    },
    {
        "id": 5,
        "name": "Информатика",
        "rang": 6,
    },
    {
        "id": 7,
        "name": "Литература",
        "rang": 5,
    },
    {
        "id": 8,
        "name": "История",
        "rang": 4,
    },
    {
        "id": 9,
        "name": "Рисование",
        "rang": 3,
    },
    {
        "id": 10,
        "name": "Музыка",
        "rang": 3,
    },
    {
        "id": 11,
        "name": "Труд",
        "rang": 2,
    },
    {
        "id": 12,
        "name": "Физическая культура",
        "rang": 1,
    }

]



GetRaspWeek() # вызов замыкающей функции
