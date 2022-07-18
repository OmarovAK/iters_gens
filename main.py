from itertools import chain

nested_list = [
    ['a', 'b', 'c'],
    ['d', 'e', 'f', 'h', False],
    [1, 2, None,
     [
         ['a', 'b', 'c'],
         ['d', 'e', 'f', 'h', False],
         [1, 2, None]
     ]
     ],
]

print('Итератор')


class My_iterator:
    def __init__(self, my_list):
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

print([item for item in my_object_class if not isinstance(item, list)])

print(30 * '=')

print('Генератор')


def gen_list(nested_list):
    for item in nested_list:
        if isinstance(item, list):
            yield from gen_list(item)
        else:
            yield item


for i in gen_list(nested_list):
    print(i)

print([item for item in gen_list(nested_list)])