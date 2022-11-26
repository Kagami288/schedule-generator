import random

iterator = 1

def GetLesson(subjects):
    subjects_weights = [subject['rang'] for subject in subjects]
    SelectSubject = random.choices(subjects, subjects_weights)[0]
    print(SelectSubject)
def GetLessons(iterator):
    while iterator <= 4:  # Генерация расписания для 1 класса
        lesson = GetLesson(subjects)
        iterator += 1
def GetRaspWeek():
    for dayWeek in DaysWeek:
        print(dayWeek["name"])
        GetLessons(iterator)



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



GetRaspWeek()
