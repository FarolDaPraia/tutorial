'''create an iterator using a class'''

class Sequence:
    def __init__(self, sequence):
        self.words = sequence.split()
        self.index = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.index >= len(self.words):
            raise StopIteration
        index = self.index
        self.index += 1
        return self.words[index]



sequence = Sequence('This is a test')

for word in sequence:
    print(word)

## Iterators and Iterables difference 

def better_grouper(inputs, n):
    iters = [iter(inputs)] * n
    return zip(*iters)

nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
teste = better_grouper(nums, 2)
for ele in teste:
    print('teste')
    print(ele)

def better_grouper2(inputs, n):
    iters = [inputs] * n
    return zip(*iters)

teste2 = better_grouper2(nums, 2)
for ele in teste2:
    print('teste2')
    print(ele)
