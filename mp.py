import time
from multiprocessing import Process, Manager, Value

def foo1(data, y):
    while(abs(data.value)<3):
        print(f"{data.value}, p1")
        y.value += 1
        data.value -= 1
        time.sleep(.1)

def foo2(data,y):
    while(abs(data.value)<3):
        print(f"{data.value}, p2")
        y.value += 1
        data.value += 1
        time.sleep(.1)

if __name__ == "__main__":
    manager = Manager()
    x = Value('i', 0)
    y = Value('i', 0)

    # for i in range(5):
    p1 = Process(target=foo1, args=(x, y))
    p2 = Process(target=foo2, args=(x, y))

    print ('Before waiting: ')
    print ('x = {0}'.format(x.value))
    # print ('x = {0}'.format(y.value))

    p1.start()
    p2.start()

    p1.join()
    p2.join()

    print ('After waiting: ')
    print ('x = {0}'.format(x.value))
    print ('y = {0}'.format(y.value))