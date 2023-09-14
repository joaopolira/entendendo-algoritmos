

class MyStack:
    def __init__(self):
        self.numbers = []
        self.count = 0

    def push(self, number):
        self.count = self.count + 1
        self.numbers.append(number)

    def pop(self):
        number = self.numbers[self.count-1]
        self.numbers.remove(self.count)
        self.count = self.count - 1
        return number

    def contains(self, number):
        for n in self.numbers:
            if n == number:
                return True
        return False
