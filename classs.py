class Hero():
    def __init__(self, name, ability):
        self.name = name
        self.ability = ability

class Hero_super(Hero):

    def __str__(self):
        return f'name: {self.name}\n'\
               f'ability: {self.ability}'

    def print_phrase(self):
        print(f'{self.name} it is super_hero')

