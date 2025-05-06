from random import random
from Enemy import Enemy


class ShangTsung(Enemy):
    def __init__(self, health_points, attack_damage):
        super().__init__(
            type_of_enemy="ShangTsung",
            health_points=health_points,
            attack_damage=attack_damage,
        )

    def talk(self):
        print("Shang Tsung - Your soul is mine")

    def combo_hits(self):
        print("Shang Tsung - Combo hits by 35 hp")

    def special_attack(self):
        did_special_attack_work = random() < 0.50
        if did_special_attack_work:
            self.attack_damage += 12
            print("Shang Tsung make special_attack hit plus 12")
