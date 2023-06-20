import threading
import time

ls = []


def count(n):
    for i in range(1, n + 1):
        ls.append(i)
        time.sleep(0.01)
    return "Count"


def worker(n):
    for i in range(1, n + 1):
        ls.append(i)
        time.sleep(0.02)
    return "Worker"


x = threading.Thread(target=worker, args=(5,))
x.start()

for _ in range(2):
    y = threading.Thread(target=count, args=(10,))
    y.start()

print("Threads:", threading.active_count())

# synchronize threads
x.join()
y.join()

print("Worker:", ls)


class CustomThread(threading.Thread):
    def __init__(self, threadId, name, count):
        super().__init__()
        self.threadId = threadId
        self.name = name
        self.count = count

    def run(self):
        print("Starting:", self.name, "\n")
        threadLock.acquire()
        print_time(self.name, 1, self.count)
        threadLock.release()
        print("Exiting", self.name, "\n")


class CustomThread2(CustomThread):
    def __init__(self, threadId, name, count):
        super().__init__(threadId, name, count)

    def run(self):
        print("Starting:", self.name, "\n")
        threadLock.acquire()
        threadLock.release()
        print_time(self.name, 1, self.count)
        print("Exiting", self.name, "\n")


def print_time(name, delay, count):
    while count:
        time.sleep(delay)
        print(name, time.ctime(time.time()), "\n")
        count -= 1


threadLock = threading.Lock()

x = CustomThread(1, "Payment", 5)
y = CustomThread2(2, "Send Email", 10)
z = CustomThread2(3, "Load Page", 3)

x.start()
y.start()
z.start()
x.join()
y.join()
z.join()

print("Exiting Main Thread")
