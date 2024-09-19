from abc import ABC, abstractmethod


class Weapon(ABC):              # Абстрактный класс оружия
    def __init__(self, name):   # Для того чтобы задавать оружию имя на кириллице (для отображения в консоли)
        self.name = name

    @abstractmethod
    def attack(self):           # Абстрактный метод атаки
        pass


# Класс меч
class Sword(Weapon):
    def __init__(self):
        super().__init__("меч")

    def attack(self):
        return "ВЖУХ мечём!"       # Теперь спокойно назначаем для меча свой уникальный тип атаки


# Класс лук
class Bow(Weapon):
    def __init__(self):
        super().__init__("лук")

    def attack(self):
        return "Стреляет из лука!"  # Для лука назначаем другой тип атаки


# Класс - воин
class Fighter:
    def __init__(self, name):
        self.name = name
        self.weapon = None  # Оружие по умолчанию не выбрано

    # Метод смены оружия
    def change_weapon(self, weapon: Weapon):
        self.weapon = weapon
        print(f"{self.name} теперь использует {self.weapon.name}.")

    # Простой механизм демонстрации боя
    def fight(self, monster):
        if self.weapon:
            print(f"{self.name} бьётся с {monster}. {self.weapon.attack()}")
            print(f"{self.name} попадает по {monster}.")


# Класс - монстр
class Monster:
    def __init__(self, name):
        self.name = name

    def __str__(self):          # Для корректного отображения имени монстра в консоли
        return self.name

# Тестирование и демонстрация

fighter = Fighter("Пендальф")
monster = Monster("Балрог")

sword = Sword()
fighter.change_weapon(sword)

fighter.fight(monster)

bow = Bow()
fighter.change_weapon(bow)

fighter.fight(monster)

"""
Добавить новый тип оружия можно не затрагивая воинов и механизм боя:

 class 'придумать'(Weapon):
     def __init__(self):
         super().__init__("задать имя")

     def attack(self):
         return "придумать как оружие будет применяться"

Ни одна из этих строчек не трогает ничего и никого кроме родительского класса weapon, который абстрактный
и представляет из себя шаблон и заглушен pass.
"""



