from player import Player
from enemy import Enemy, Bone_Snacher, Blood_Drinker, king_Vampire

zain = Player('zain')

zain.lives -= 1
print(zain)
zain.lives -= 1
print(zain)
zain.lives -= 1
print(zain)

zain.level += 1
print(zain)
zain.level += 2
print(zain)

zain.level -= 3
print(zain)

zain.level -= 2
print(zain)

print('x'*20)
print('----------Enemy damage Work-------')
racoon = Enemy('Racoon')
print(racoon)

racoon.take_damage(2)
print(racoon)

racoon.take_damage(2)
print(racoon)

racoon.take_damage(2)
print(racoon)

print('x'*20)
print('----------Inheritance Work-------')


# Method overloading (changed method in the child class)
ugly_snacher = Bone_Snacher('ugly snacher',5,2)
print(ugly_snacher)
# ugly_snacher.snach()

# while ugly_snacher.lives:
#     ugly_snacher.snach()
#     ugly_snacher.take_damage(2)
   
# print(ugly_snacher)
# 

print('x'*30)

print('-------------Another Enemy class in action-----------------')

vampire = Blood_Drinker('Vampire', 10, 4)
print(vampire)
while vampire.lives:
    vampire.take_damage(2)

print(vampire)

print('---------------------Another Enemy class in action-----------------')

king_vampire = king_Vampire('King Vampire', 30, 4)
print(king_vampire)
while king_vampire.lives:
    king_vampire.take_damage(3)
print(king_vampire)
