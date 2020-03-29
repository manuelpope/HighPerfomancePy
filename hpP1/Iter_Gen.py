print("test no 1")
class myIter:
    def __init__(self, finalCondition, multi):
        self.finalN = finalCondition
        self.multi = multi

    # iter function
    def __iter__(self):
        self.curr = 0
        return self

    def __next__(self):
        if self.curr <= self.finalN:
            multiple = self.curr
            self.curr += self.multi
            return multiple
        else:
            raise StopIteration


initIterator = myIter(20, 5)  # crea la condicion final y el aumento
iterObj = iter(initIterator)
# asigna el obj iter a el iterador
# iterar...
print(next(iterObj))
print(next(iterObj))
print(next(iterObj))
print(next(iterObj))
print(next(iterObj))


# es una simple clase que guarda el estado del iterador , asi no se
# desborda la memoria


# GENERATOR

def myGenerator():
    x = 5
    y = 6
    print('halted')
    yield x, y
    print('resume')
    x += y
    print('halted')
    yield x, y
    print('resume')
    x += 1
    y += 10
    yield x, y


for x, y in myGenerator():
    print(x, y)
