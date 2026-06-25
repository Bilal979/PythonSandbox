import random
class Enemy:
    
    def __init__(self, name='enemy', hit_points=4, lives=1):
        self.name = name
        self.hit_points = hit_points
        self.remaining_hit_points = hit_points
        self.lives = lives

    
    def take_damage(self, damage):
        self.remaining_hit_points = self.remaining_hit_points - damage

        if self.remaining_hit_points > 0:
            print(f'I took bullet with {damage} damage, remianing hit points {self.remaining_hit_points}')
        else:
            self.remaining_hit_points = 0
            self.lives -= 1
            if self.lives > 0:
                self.remaining_hit_points = self.hit_points
                print(f"{self.name} lost a life, I have {self.lives} lives left")
            else:
                print(f'Argghhh, {self.name} died!')

    def __str__(self):
        return f'Name: {self.name}, Hit Points: {self.remaining_hit_points}, Lives: {self.lives}'


class Bone_Snacher(Enemy):
    def __init__(self,name, hit_points=4, lives=1):
        super().__init__(name=name, hit_points=hit_points, lives=lives)

    
    def snach(self):
        print(f'{self.name} is snaching your bones!')

class Blood_Drinker(Enemy):
    def __init__(self, name, hit_points=10, lives=3):
        super().__init__(name=name, hit_points=hit_points, lives=lives)

    def drink(self):
        print(f"{self.name} is drinking your blood")

    def dodge(self):
        if random.randint(1,5) == 3:
            print(f"***Haa, {self.name} dodged the bullet***")
            return True
        else:
            return False

    
    def take_damage(self, damage):
        if not self.dodge():
            super().take_damage(damage)
        

class king_Vampire(Blood_Drinker):
    def __init__(self, name, hit_points=30, lives=4):
        super().__init__(name=name, hit_points=hit_points, lives=lives)

    def take_damage(self, damage):
        print(f"{self.name} was shoot with damage {damage}")
        super().take_damage(damage//3)

