# importing the modules
from threading import *
import time
import random

# multiple readers can read at a time
mutex = Semaphore(1)
rw_mutex = Semaphore(1)
# only one writers can write at a time
read_count = 0

data = []


# reader function , it is popping the data from the data list one by one
def reader(name):
    global read_count
    # calling acquire method
    i = 0
    while i < random.randint(0, 9):
        mutex.acquire()
        read_count = read_count + 1
        if read_count == 1:
            rw_mutex.acquire()
        mutex.release()
        if len(data):
            print(data.pop(), "consumed", name)
            time.sleep(1)
        mutex.acquire()
        read_count = read_count - 1
        if read_count == 0:
            rw_mutex.release()
        mutex.release()
        i = i + 1


# reader function

def writer(name):

    # calling acquire method
    i = 0
    while i < random.randint(0, 9):
        rw_mutex.acquire()
        x = random.randint(0, 9)
        data.append(x)

        time.sleep(1)
        print(x, "produced", name)
        rw_mutex.release()
        i = i + 1


interrupted = False

# creating multiple thread
t1 = Thread(target=writer, args=('Writer-1', ))
t2 = Thread(target=writer, args=('Writer-2', ))
t3 = Thread(target=writer, args=('Writer-3', ))
t4 = Thread(target=reader, args=('Reader-1', ))
t5 = Thread(target=reader, args=('Reader-2', ))
t6 = Thread(target=reader, args=('Reader-3', ))

# calling the threads
t2.start()
t1.start()
t6.start()
t3.start()
t4.start()
t5.start()

t1.join()
t2.join()
t3.join()
t4.join()
t5.join()
t6.join()
print(data)