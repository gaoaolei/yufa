class Cc(object):
    @property
    def score(self):
        return self._score
    @score.setter
    def score(self, value):
        if not isinstance(value, int):
            raise ERR('bushizhengshu')
        if value < 0 or value > 100:
            raise ERR('fanweiyouwu')
        self._score = value
c=Cc()
c._score = 60
print c._score



