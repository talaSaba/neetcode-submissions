class MyHashSet:

    def __init__(self):
        self.hash = {}

    def add(self, key: int) -> None:
        self.hash[key] = 0

    def remove(self, key: int) -> None:
        if key in self.hash:
            del self.hash[key]

    def contains(self, key: int) -> bool:
        return key in self.hash