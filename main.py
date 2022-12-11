import random
import School_class as SClass

def get_lesson(subjects):
    """Randomly selects a subject from the given list of subjects, and returns it."""
    # Select a random subject, making sure that it has not been used up
    subject = random.choices(subjects, [subject['rang'] for subject in subjects])[0]
    while subject['hours'] <= 0:
        subject = random.choices(subjects, [subject['rang'] for subject in subjects])[0]

    # Decrement the number of hours remaining for the selected subject
    index = subjects.index(subject)
    subjects[index]["hours"] -= 1

    return subject

def get_lessons(subjects, num_lessons=4):
    """Returns a list of random lessons, with a length equal to the given number of lessons."""
    lessons = []
    for i in range(num_lessons):
        lessons.append(get_lesson(subjects))
    return lessons

def get_rasp_week():
    """Generates a weekly schedule for a school class."""
    OneA = SClass.SchoolClass(1, "A")
    OneA.get_info_class()
    for dayWeek in DaysWeek:
        print(dayWeek["name"])
        lessons = get_lessons(subjects)
        for lesson in lessons:
            print(lesson)


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
        "hours": 5,
    },
    {
        "id": 2,
        "name": "Русский",
        "rang": 7,
        "hours": 4,
    },
    {
        "id": 3,
        "name": "Английский",
        "rang": 7,
        "hours": 1,
    },
    {
        "id": 4,
        "name": "Природоведение",
        "rang": 6,
        "hours": 2,
    },
    {
        "id": 5,
        "name": "Информатика",
        "rang": 6,
        "hours": 1,
    },
    {
        "id": 7,
        "name": "Литература",
        "rang": 5,
        "hours": 4,
    },
    {
        "id": 8,
        "name": "История",
        "rang": 4,
        "hours": 1,
    },
    {
        "id": 9,
        "name": "Рисование",
        "rang": 3,
        "hours": 1,
    },
    {
        "id": 10,
        "name": "Музыка",
        "rang": 3,
        "hours": 1,
    },
    {
        "id": 11,
        "name": "Труд",
        "rang": 2,
        "hours": 1,
    },
    {
        "id": 12,
        "name": "Физическая культура",
        "rang": 1,
        "hours": 3,
    }

]



get_rasp_week() # вызов замыкающей функции
