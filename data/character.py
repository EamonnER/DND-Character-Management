from math import floor, ceil
from json import load

class_data_json = open('classes/classes.json')
class_data = load(class_data_json)


class Character:
    def __init__(self, classes: dict[str: int], ability_scores: dict[str: int]):
        self.level: int = 0
        self.max_hp: int = 0
        self.proficiency_bonus: int = 0
        self.saving_throw_proficiencies: list[str] = []
        self.classes: dict[str: int] = classes
        self.ability_scores: dict[str: int] = ability_scores

        """ Sets values correctly """
        # Loops through each class the character has
        for Class in self.classes:
            class_level = self.classes[Class]

            # Loops for each level the character has in that class
            for level in range(0, class_level):
                self.level_up(Class)

        self.update_max_hp()
        self.update_proficiency_bonus()

    """ Setters """
    def set_ability_score(self, ability: str, score: int):
        self.ability_scores[ability] = score

    def increase_ability_score(self, ability: str, amount: int):
        self.ability_scores[ability] += amount
        if ability == "con":
            self.update_max_hp()

    def level_up(self, Class: str):
        """ Levels up a specific class """
        if Class not in self.classes:
            self.classes[Class] = 0

        self.classes[Class] += 1

        self.level = 0
        for Class in self.classes:
            self.level += self.classes[Class]

    def update_max_hp(self):
        """ Correctly sets the max HP of the character based on their class levels """
        self.max_hp = 0
        con_mod = self.get_ability_mod("con")

        # Cycles through each class the character has
        for Class in self.classes:
            class_level = self.classes[Class]
            hit_dice = class_data[Class]["hit_dice"]

            # Gets the level 1 hp that class gets
            self.max_hp += hit_dice + con_mod

            # Loops for each level the character has in that class
            for level in range(0, class_level):
                self.max_hp += ceil((hit_dice + 1) / 2)

    def update_proficiency_bonus(self):
        """ Gets the proficiency bonus of the character, based on their class levels """
        highest_class_level = self.get_highest_class_level()[1]

        # Calculates the proficiency bonus that class gets
        self.proficiency_bonus = ((highest_class_level-1)//4) + 2

    """ Getters """
    def get_ability_mod(self, ability) -> int:
        ability_score = self.ability_scores[ability]
        return (ability_score-10)//2

    def get_highest_class_level(self) -> (str, int):
        Class = max(self.classes, key=self.classes.get)
        level = self.classes[Class]
        return Class, level
