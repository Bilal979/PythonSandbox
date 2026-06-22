from player import Player
from enemy import Enemy, Bone_Snacher

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
ugly_snacher = Bone_Snacher('ugly snacher',18,4)
print(ugly_snacher)
ugly_snacher.snach()

# 