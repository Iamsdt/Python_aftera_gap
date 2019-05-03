import time
import _thread


def timer(name, delay):
    i = 0
    while i < 5:
        time.sleep(delay)
        print(name + ":" + time.asctime())
        i += 1


try:
    _thread.start_new_thread(timer, ("Thread 1", 2))
    _thread.start_new_thread(timer, ("Thread 2", 4))
except RuntimeError:
    print("Unable to start")

time.sleep(10)
