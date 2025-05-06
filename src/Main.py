from Enemy import Enemy
from Hero import Hero
from ShangTsung import ShangTsung
from Weapon import Weapon


def battle(shang_tsung: Enemy, hero: Hero):
    shang_tsung.talk()
    hero.attack()
    shang_tsung.attack()
    shang_tsung.special_attack()

    hero.attack()


shang_tsung = ShangTsung(100, 18)
hero = Hero(120, 10)
weapon = Weapon("Axe", 25)
hero.weapon = weapon
hero.equip_weapon()

battle(shang_tsung, hero)