import math
import time
from datetime import datetime
from multiprocessing import Process, connection, current_process

a = []
b = []
c = []


def calc1(numbers):
    for number in numbers:
        a.append(math.sqrt(number**3))
    print(f"{datetime.now()} {current_process().name} exiting")


def calc2(numbers):
    for number in numbers:
        b.append(math.sqrt(number**4))
    print(f"{datetime.now()} {current_process().name} exiting")


def calc3(numbers):
    for number in numbers:
        c.append(math.sqrt(number**5))
    print(f"{datetime.now()} {current_process().name} exiting")


if __name__ == "__main__":
    numbers = list(range(1, 5000000))
    p1 = Process(target=calc1, args=(numbers,))
    p2 = Process(target=calc2, args=(numbers,))
    p3 = Process(target=calc3, args=(numbers,))

    start = time.time()
    pool = [p1, p2, p3]
    for p in pool:
        p.start()

    print(f"{datetime.now()} {current_process().name} waiting")
    connection.wait(p.sentinel for p in pool)
    print(f"{datetime.now()} {current_process().name} unblocked")

    end = time.time()
    print("Time taken in seconds: ", end - start)
