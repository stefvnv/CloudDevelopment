class Book:

    def __init__(self, title, author):
        self._title = title
        self._author = author

    def getTitle(self):
        return self._title

    def getAuthor(self):
        return self._author

    def setAuthor(self, author):
        self._author = author


class Audio:

    def __init__(self, format, playingTime):
        self._format = format
        self._playingTime = playingTime

    def getPlayingTime(self):
        return self._playingTime

    def getFormat(self):
        return self._format

    def setFormat(self, format):
        self._format = format

    def setPlayTime(self, playingTime):
        self._playingTime = playingTime

    # Extended Class


class AudioBook(Book, Audio):

    def __init__(self, title, author, format, pT, Is):
        Book.__init__(self, title, author)
        Audio.__init__(self, format, pT)
        self.__isbn = Is

    def addToPlayingTime(self, time):
        self._playingTime += time

    def getIsbn(self):
        return self.__isbn
