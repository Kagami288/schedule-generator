import random
import School_class as SClass
import interface as IF

iterator = 1 #отвечает за количество генерируемых уроков

def GetLesson(subjects):# случайная выборка из subjects
    check = False # Нужна для while
    subjects_weights = [subject['rang'] for subject in subjects] # перебор объекта по рангу трудности / можно поменять критерий на имя или id
    while check == False:
        SelectSubject = random.choices(subjects, subjects_weights)[0] # рандомно выбирает по id
        if SelectSubject["hours"] > 0: 
            index = subjects.index(SelectSubject) # находит индекс выбранного предмета     
            subjects[index]["hours"]-=1 # вычитает из часов использованный урок
            check = True
            return SelectSubject # возвращает предмет
def GetLessons(iterator): # получаем уроки с GetLesson5
    lesson = []                                        # решил объявить списком для удобства
    while iterator <= 4:  # генерация расписания для одного
        lesson.append(GetLesson(subjects)) #добавляет урок в список
        iterator += 1
    return lesson
def GetRaspWeek(): # генерируем раписание по неделям
    OneA = SClass.School_Class(1,"A")
    OneA.get_infoClass()
    for dayWeek in DaysWeek: # перебор дней недели
        print(dayWeek["name"]) # вывод дня недели
        IF.ui.Print_TimeTable(dayWeek["name"])
        lessons = GetLessons(iterator)
        for lesson in lessons:
            print(lesson) # вывод 4 уроков




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



GetRaspWeek() # вызов замыкающей функции
