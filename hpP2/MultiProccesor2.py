print('multi processing python')

#GIL
#quien maneja todo este mierdero de threads ops, simplifica memoria usage
#se caga el paralelismo, no !   dejacorrer varios al mismo tiempo


#totalmente diferente multi processing
# processorX has memoryX, couldnt share memory but could be join manually
# by global variables at the end
import  time
import numpy
from multiprocessing import Process, Pool
from common.CommonFuncTesting import funcSimple, funcSquare,funcCube

def fSimple(l):
    sum = 0
    for i in range(0,l):
        sum +=i
    print(sum)

def fSquare(l):
    sum = 0
    for i in range(0,l):
        sum +=i**2
    print(sum)


def fCube(l):
    sum = 0
    for i in range(0,l):
        sum +=i**3
    print(sum)

def logExp(x):
    return numpy.log(x)


def doSomething():
    lenght = 5000000
    processSimple = Process(target = funcSimple, args=(lenght,))
    processSquare = Process(target = fSquare, args=(lenght,))
    processCube = Process(target = fCube, args=(lenght,))

    processCube.start()
    processSimple.start()
    processSquare.start()


    processCube.join()
    processSimple.join()
    processSquare.join()
#map is sync and lock each processor , async could be quicker.
if __name__ == "__main__":
    doSomething()
    start = time.time()
    pool= Pool(processes= 8)
    inputList = [elem for elem in range (1,10000000)]
    result = pool.map_async(logExp ,inputList)
    end = time.time()
    print(end - start , "seconds")