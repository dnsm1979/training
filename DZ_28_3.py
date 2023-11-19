import copy


class Phone:
    def __init__(self, memory, model, color, type, os):
        self.memory = memory
        self.model = model
        self.color = color
        self.type = type
        self.os = os

    def __str__(self):
        return f'{self.type} {self.model} {self.memory} {self.os} {self.color}'

    def clone(self):
        return copy.deepcopy(self)


original_phone = Phone('64GB', 'iPhone', 'White', 'smartphone', 'IOS')
print('Original Phone:', original_phone)

cloned_phone = original_phone.clone()
print('Cloned Phone:', cloned_phone)