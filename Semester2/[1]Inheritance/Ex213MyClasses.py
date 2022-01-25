class Team:

    def __init__(self, name):
        self._name = name
        self._points = 0
        self._played = 0

    def draw(self):
        self._played += 1
        self._points += 1

    def loss(self):
        self._played += 1
        self._points += 0

    def getName(self):
        return self._name

    def getPlayed(self):
        return self._played

    def getPoints(self):
        return self._points


# Extended Class
class FootballTeam(Team):

    def __init__(self, name):
        super().__init__(name)
        self.__wins = 0

    def win(self):
        self._points += 3
        self.__wins += 1
        self._played += 1

    def getWins(self):
        return self.__wins
