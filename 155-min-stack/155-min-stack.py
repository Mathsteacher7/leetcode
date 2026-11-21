class MinStack:
    def __init__(self):
        self.stack_object = []
        self.min_list = []

    def push(self, value: int) -> None:
        self.stack_object.append(value)
        min_value = value if not self.min_list else min(value, self.min_list[-1])
        self.min_list.append(min_value)

    def pop(self) -> None:
        self.stack_object.pop()
        self.min_list.pop()

    def top(self) -> int:
        return self.stack_object[-1]

    def getMin(self) -> int:
        return self.min_list[-1]
