import copy
from typing import List

class SchoolClass:

    def __init__(self, num: int, parallel: int) -> None:
        self.num = num
        self.parallel = parallel
        self.time_table = []

    def set_time_table(self, time_table: List[str]) -> None:
        self.time_table = time_table

    def get_info_class(self) -> str:
        return f"Учебный класс: {self.num}{self.parallel}"

    def get_time_table(self) -> List[str]:
        return self.time_table
