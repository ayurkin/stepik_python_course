import time

class Loggable:
    def log(self, msg):
        print(str(time.ctime()) + ": " + str(msg))

class LoggableList(Loggable, list):
    def append(self, x):
        super(LoggableList, self).append(x)
        super(LoggableList, self).log(x)



c = LoggableList([1, 2, 3])
c.append(19)
print(c)