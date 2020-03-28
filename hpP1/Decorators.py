import time
import Lambda
def func1():
    print(1)
def myDecor(func):
    #modified func , args para hacerlo dinamico con o sin argumentos

    def deco_func( *args, **kwargs):
        print(2)
        func(*args, **kwargs)
        print(3)
    return deco_func

newFunc= myDecor(func1)
newFunc()

@myDecor # permite incertar esta funcion en el decorator
def otherFunc(x,y,z):
    print(4)
    print(x,y,z)

otherFunc(5,6,7)


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


Lambda.

createBigBetterList(100000)
createBigList(100000)

