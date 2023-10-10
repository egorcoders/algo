import json
import random
import time

from colorama import Fore, Back, init

init(autoreset=True)


class Transformer:
    def __init__(self, id, name, hp, attack, weapon, description, war_phrase, crit, regeneration, appearance, **kwargs):
        self.id = id
        self.name = name
        self.hp = hp
        self.attack = attack
        self.weapon = weapon
        self.description = description
        self.war_phrase = war_phrase
        self.crit = crit
        self.regeneration = regeneration
        self.appearance = appearance

    def fight(self, transformer):
        damage = self.attack * self.crit
        self.check_crit(damage)
        transformer.hp -= damage
        print(f'{self.name} использует {self.weapon}, нанеся трансформеру {transformer.name} урон {round(damage, 2)}!')
        print(f'У {transformer.name} осталось {round(transformer.hp, 2)} здоровья!\n')

        if not self.hp > 0 or not transformer.hp > 0:
            if not self.hp > 0:
                fallen, winner = self, transformer
            else:
                fallen, winner = transformer, self

            print(Back.RED + Fore.BLACK + f'{fallen.name} пал от рук {winner.name}')
            print(f'{fallen.name} будет отомщен!\n')
            reg = winner.regeneration * winner.hp
            winner.hp += reg
            print(f'{winner.name} удалось восстановить {round(reg, 2)} здоровья!')

    def is_alive(self):
        return self.hp > 0

    def check_crit(self, crit):
        if 10 > crit > 0:
            print(Fore.GREEN + f'{self.name} с КРИТОМ {round(crit, 2)} НИЧЕГО НЕ МОЖЕТ!')
        elif 30 > crit > 10:
            print(Fore.YELLOW + f'{self.name} с УДАРОМ {round(crit, 2)} УДАРИЛ СЗАДИ!')
        elif crit > 30:
            print(Fore.RED + f'{self.name} с ЛОВКОСТЬЮ {round(crit, 2)} КРИТАНУЛ!')

    def check_health(self, transformer):
        if not (self.is_alive() and transformer.is_alive()):
            healthy = self if self.hp > transformer.hp else transformer
            if 150 > healthy.hp > 90:
                print(Back.GREEN + Fore.BLACK + f'{healthy.name} с {round(healthy.hp, 2)} hp ЧУВСТВУЕТ СИЛУ!')
            elif 200 > healthy.hp > 150:
                print(Back.GREEN + Fore.BLACK + f'{healthy.name} {round(healthy.hp, 2)} hp МОГУЩЕСТВЕН!')
            elif healthy.hp > 200:
                print(Back.GREEN + Fore.RED + f'{healthy.name} {round(healthy.hp, 2)} hp НЕ БОИТСЯ БОГОВ!!!')

    def start(self):
        print(f'{self.name}! {self.appearance}\n')


    def __repr__(self):
        return f'{self.name}! {self.description}'

    def end(self):
        print(self)


transformers = []
print('Да начнется битва трансформеров!\n')
time.sleep(1)

with open('data.json', 'r', encoding='utf-8') as f:
    json_transformers = json.load(f)
    for j in json_transformers:
        transformers.append(Transformer(**j))

t1 = t2 = None

while transformers:

    random.shuffle(transformers)

    if t1 is None:
        t1 = transformers.pop()
        t1.start()
    if t2 is None:
        t2 = transformers.pop()
        t2.start()

    t1.fight(t2)
    if not t2.is_alive():
        t2 = transformers.pop()

    t2.fight(t1)
    if not t1.is_alive():
        t1 = transformers.pop()

    t1.check_health(t2)

    t1, t2 = t2, t1

    time.sleep(1)

win = t1 if t1.hp > t2.hp else t2
print(Back.CYAN + Fore.BLACK + f'{win} Восседает на троне трансформеров! ЭТО ПОБЕДА!')
