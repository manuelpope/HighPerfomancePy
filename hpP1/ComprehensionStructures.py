#List
import time


listNumer=[]
listNumer = [elem for elem in range(5)]
print(listNumer)
x1= [elem * 10 for elem in listNumer]
print(x1)

#Dict// elem its gonna be key and value is the ops, the for loop is for iterable group
dict = {elem:elem*elem for elem in x1}
print(dict)

x = "este es el string wow"
l= x.split(' ')
print(l)
newDict= {elem: len(elem) for elem in l}
print(newDict)

#time measures
#forma super lenta

start = time.time()
newList = []
for x in range(0 , 9000000):
    newList.append(x*2)
end = time.time()

print('time take is {} seconds'.format(end-start))

start = time.time()
newList = [elem * 2 for elem in range (0,9000000)]
end = time.time()
print('time2 take is {} seconds'.format(end-start))