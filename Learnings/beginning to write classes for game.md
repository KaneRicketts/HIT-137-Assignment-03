class Character:
    """Character's specs are determined here."""

    def __init__(self, name: str, speed: int, max_health: int, lives: int, jump: int, fly: bool) -> None:
        self.name = name
        self.speed = speed
        self.max_health = max_health
        self.lives = lives
        self.jump = jump
        self.fly = fly
    
    class Weapon:
        """Weapon specs are determined here."""

        def __init__(weapon, ID: str, damage: int, range: int, velocity: int) -> None:
            weapon.ID = ID
            weapon.damage = damage
            weapon.range = range
            weapon.velocity = velocity

    rock: Weapon = Weapon(ID = "Rock", damage = 10, range = 100, velocity = 50)
    enemy_touch: Weapon = Weapon(ID = "Touch", damage = 5, range= 0, velocity =0)
    spit: Weapon = Weapon(ID = "Spider-Spit", damage = 20, range = 100, velocity = 20)

    class Collectible:
        """Collectibles are given values here."""
        def __init__(collectible, label: str, add_points: int, add_health: int, add_lives: int,) -> None:
            collectible.label = label
            collectible.add_points = add_points
            collectible.add_health = add_health
            collectible.add_lives = add_lives

    kill: Collectible = Collectible(label = "Kill", add_points = 5, add_health = 0, add_lives = 0)
    coin: Collectible = Collectible(label = "Coin", add_points = 10, add_health = 0, add_lives = 0)
    fruit: Collectible = Collectible(label = "Coin", add_points = 0, add_health = 20, add_lives = 0)
    heart: Collectible = Collectible(label = "Coin", add_points = 0, add_health = 0, add_lives = 1)

    class HealthBar:
        """The size and view of the Health Bar is defined here."""

        def __init__(self, name: str, pos_x_y: tuple, size_x: int, size_y: int, colour_background: str, colour_remaining: str) -> None:
            self.name = name
            self.pos_x_y = pos_x_y
            self.size_x = size_x
            self.size_y = size_y
            self.colour_background = colour_background
            self.colour_remaining = colour_remaining

        def display():
            position
            height
            width of full health
            width of remaining health

        def current_health():
            # at start, current health = max health
            # once "something happens", then check current health
            
            current_health += -(damage) + add_health
            return current_health
    
herbert: Character = Character(name = "Herbert", speed = 5, max_health = 100, lives = 3, jump = 10, fly = False)
bug_enemy: Character = Character(name = "Bug", speed = 4, max_health = 10, lives = 1, jump = 0, fly = False)
bat_enemy: Character = Character(name = "Bat", speed = 4, max_health = 20, lives = 1, jump = 0, fly = True)
boss_enemy: Character = Character(name = "Spider", speed = 5, max_health = 50, lives = 2, jump = 10, fly = False)


"""
How to reference class from class.
class ClassA:
    def method_a(self):
        print("Method A")

class ClassB:
    def method_b(self):
        instance_a = ClassA()
        instance_a.method_a()  # This calls method_a of ClassA from an instance of ClassB

OR

class BigClassA:
    def __init__(self):
        ...

class BigClassB:
    def __init__(self, objA):
        self.b = objA.b
        self.c = objA.c
        self.d = objA.d

class BigClassC:
    def __init__(self, objA, objB):
        self.b = objA.b # need value of b from BigClassA
        self.f = objB.f # need value of f from BigClassB


While instantiating, do:

objA = BigClassA()
..
objB = BigClassB(objA)
..
objC = BigClassC(objA, objB)"""