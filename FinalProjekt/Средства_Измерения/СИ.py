class SI:
    #конструктор;
    def __init__(self, name, tupe, factory_name, subdivision, responsible):
        # - статус
        self.status = "Исправлен"
        # - наименование;
        self.name = name
        # - тип;
        self.tupe = tupe
        # - заводской номер;
        self.factory_name = factory_name
        # - подразделение;
        self.subdivision = subdivision
        # - ответсвенный;
        self.responsible = responsible

    def to_corrected(self):
        self.status = "Исправлен"

    def repair(self):
        self.status = "На ремонте"

    def __str__(self):
        return self.status + "-- Наименование: " + str(self.name) + "; " + "Тип: " + str(self.tupe) + "; " + "Заводской номер: " + str(self.factory_name) + "; " + "Подразделение: " + str(self.subdivision) + "; " + "Ответсвенный: " + str(self.responsible)

