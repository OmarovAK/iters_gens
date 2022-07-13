from itertools import chain

nested_list = [
    ['a', 'b', 'c'],
    ['d', 'e', 'f', 'h', False],
    [1, 2, None, ['cndks', [2525]]],
    [
        ['a', 'b', 'c'],
        ['d', 'e', 'f', 'h', False],
        [1, 2, None, ['cndks', [2525]]],
        [
            ['a', 'b', 'c'],
            ['d', 'e', 'f', 'h', False],
            [1, 2, None, ['cndks', [5555]]],
        ]
    ]
]


class My_iterator(list):

    def __init__(self, my_list):
        super().__init__()
        self.my_list = my_list

    def __iter__(self):
        self._list = iter(self.my_list)
        return self

    def __next__(self):
        next_values = next(self._list)
        if isinstance(next_values, list):
            self._list = chain(self._list, next_values)
        return next_values




my_object_class = My_iterator(nested_list)

count = 1
for i in my_object_class:
    if not isinstance(i, list):
        print(count, i)
        count = count + 1
