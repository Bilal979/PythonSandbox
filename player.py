class Player:
    def __init__(self, name, lives=3, score=0,level=1):
        self.name = name
        self._lives = lives
        self.score = score
        self._level = level

    def _get_lives(self):
        return self._lives

    def _set_lives(self, lives):
        if lives >= 0:
            self._lives = lives
        else:
            print('lives can not be less that zero')
        
    lives = property(_get_lives,_set_lives)

    def _get_level(self):
        return self._level

    def _set_level(self, level):
        if level > 0:
            delta = level - self._level
            add_score =  delta*100
            self.score = max(0, self.score + add_score)
            self._level = level
        else:
            print('Level can not be less than one')

    level = property(_get_level, _set_level)

    # The magic method to trigger on class obj creation to show its string representation
    def __str__(self):
        return f'Name: {self.name}, Lives: {self.lives}, Score: {self.score}, Level: {self.level}'


