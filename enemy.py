class Enemy:
    
    def __init__(self, name='enemy', hit_points=4, lives=1):
        self.name = name
        self.hit_points = hit_points
        self.lives = lives

    
    def take_damage(self, damage):
        remaining_points = self.hit_points - damage

        if remaining_points > 0:
            self.hit_points = remaining_points
            print(f'I took bullet with {damage} damage, remianing hit points {self.hit_points}')
        else:
            self.hit_points = 0
            self.lives -= 1
            print('Argghhh, I died!')

    def __str__(self):
        return f'Name: {self.name}, Hit Points: {self.hit_points}, Lives: {self.lives}'


class Bone_Snacher(Enemy):
    def __init__(self,name, hit_points=4, lives=1):
        super().__init__(name=name, hit_points=hit_points, lives=lives)

    
    def snach(self):
        print(f'{self.name} is snaching your bones!')
        