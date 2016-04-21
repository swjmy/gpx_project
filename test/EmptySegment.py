class EmptySegment(Exception):
    def __init__(self,str):
        self._str=str

    def __str__(self):
        return self._str
