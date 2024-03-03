class Jar:
    def __init__(self, capacity=12):
        if int(capacity) < 0:
             raise ValueError("Missing name")

    def __str__(self):
        ...

    def deposit(self, n):
        ...

    def withdraw(self, n):
        ...

    @property
    def capacity(self):
        ...

    @property
    def size(self):
        ...