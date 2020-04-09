print('multi processing python')

#GIL
#quien maneja todo este mierdero de threads ops, simplifica memoria usage
#se caga el paralelismo, no !   dejacorrer varios al mismo tiempo


#totalmente diferente multi processing
# processorX has memoryX, couldnt share memory but could be join manually
# by global variables at the end
from multiprocessing import Process
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

if __name__ == "__main__":
    doSomething()
