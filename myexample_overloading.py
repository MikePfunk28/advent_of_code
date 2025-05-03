class MyIterable:
    def __init__(self, data):
        self.data = data
        self.current_index = 0

    def __iter__(self):
        print(f"Calling __iter__ {self.__iter__}")
        return self

    def __next__(self):
        if self.current_index < len(self.data):
            item = self.data[self.current_index]
            self.current_index += 1
            print(
                f"Calling __next__ {self.__next__} {item} {self.current_index}")
            return item
        else:
            raise StopIteration


# Creating an instance of MyIterable
mys_list = [1, 9, 6, 8, 2, 9, 4, 7, 3, 4, 5]
my_iterable = MyIterable(mys_list)

# Iterating over the instance in a for loop
for item in my_iterable:
    print(item)

    print(my_iterable)
