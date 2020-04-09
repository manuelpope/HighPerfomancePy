import time
import functools

def timeDeco(funcX):
    def funcDecorated(*args,**kwargs):
        start = time.time()
        funcX(*args,**kwargs)
        end= time.time()
        print("time was {} seconds".format(end-start))
    return funcDecorated


@timeDeco
def createBigList(size):
    newList= []
    for i in range(0,size):
        newList.append(i)



@timeDeco
def createBigBetterList(size):
    return [x for x in range(0,size)]


def funcSimple (lenght):
    sum = functools.reduce(lambda a,b : a+b,[elem for elem in range(0, lenght)])
    print(sum)
    return sum


def funcSquare (lenght):
    sum = functools.reduce(lambda a,b : a+b**2,[elem for elem in range(0, lenght)])
    return sum

def funcCube (lenght):
    sum = functools.reduce(lambda a,b : a+b**3,[elem for elem in range(0, lenght)])
    return sum
