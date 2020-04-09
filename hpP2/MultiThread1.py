print('multi parallel processing python')

from threading import Thread, Lock,RLock
threadLock= Lock()

#Bad Practice-global variables

myGlobalString = "HELLO WORLD"

def addPrefix(prefixToAdd):
   global myGlobalString
   threadLock.acquire()
   myGlobalString = prefixToAdd+" "+myGlobalString
   threadLock.release()

def addSufix(sufixToAdd):
    global myGlobalString
    threadLock.acquire()
    myGlobalString = myGlobalString+sufixToAdd
    threadLock.release()

def doSomething():
    threadPrefix = Thread(target= addPrefix,args=("Adali",))
    threadSufix = Thread(target= addSufix,args=(" bye",))

    threadPrefix.start()
    threadSufix.start()

    threadPrefix.join()
    threadSufix.join()
    global myGlobalString
    print("final string is {}".format(myGlobalString))

doSomething()
#se puede bloquear , no es lo mejor....
#para evitar esto se debe usar re entrant lock - RLock

myReentrantLock = RLock()
myReentrantLock.acquire()
myGlobalString = "holaaaa foes"
#con lso conecionales no podemos hacer varios acquires
myReentrantLock.acquire()
myGlobalString += " nos fuimos"
myReentrantLock.release()
myReentrantLock.release()
print(myGlobalString)


#locks are for thread sync
