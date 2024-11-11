# generateur
class MyGen():
    current = 0

    def __init__(self, start=0, end=10) -> None:
        self.start = start
        self.end = end

    def __iter__(self):
        return self

    def __next__(self):
        if MyGen.current < self.end:
            num = MyGen.current
            MyGen.current += 1
            return num
        raise StopIteration


gen = MyGen(0, 100)
for item in gen:
    print(item)
