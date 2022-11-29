import copy
class School_Class:
    num = 0
    parallel = 0
    TimeTable = []

    def __init__(self,num, parallel) -> None:
        self.num = num
        self.parallel = parallel

    def set_TimeTable(self,TimeTable):
        self.TimeTable = copy.deepcopy(TimeTable)

        
    def get_infoClass(self):
        print(f"Учебный класс: {self.num}{self.parallel}")
    
    # def get_NameSClass(self):
    #     print(f"Учебный класс: {self.num}{self.parallel}")

    def get_TimeTable(self):
        pass
