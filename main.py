from player import Player
from enemy import Enemy

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