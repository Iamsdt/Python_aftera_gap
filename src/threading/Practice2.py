import threading


class MyThread(threading.Thread):

    def __init__(self,id,name,counter):
        threading.Thread.__init__(self)
        self.threadID = id
        self.name = name
        self.counter = counter
    
