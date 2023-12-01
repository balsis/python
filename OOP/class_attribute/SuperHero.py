class SuperHero:
    pass


batman = SuperHero()
batman.can_fly = False
batman.damage = 175

print(batman.__dict__)

superman = SuperHero()
superman.can_fly = True
superman.damage = 285
superman.alter_ego = 'Кларк Кент'
print(superman.__dict__)
