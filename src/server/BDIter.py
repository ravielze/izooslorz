"""BDIter as Bidirectional Iteration."""

class biiter(object):
    """Bidirectional iterator."""

    def __init__(self, collection: list):
        self.__T = collection
        self.__maxidx = len(collection)-1
        self.__idx = 0

    def hasNext(self):
        return self.__idx <= self.__maxidx

    def hasPrev(self):
        return self.__idx-1 >= 0

    def next(self):
        try:
            result = self.__T[self.__idx]
            self.__idx += 1
        except IndexError:
            raise StopIteration
        return result

    def prev(self):
        self.__idx -= 1
        if self.__idx < 0:
            raise StopIteration
        return self.__T[self.__idx]

    def getList(self):
        return self.__T

    def copy(self):
        return biiter(self.__T)

    def __iter__(self):
        return self