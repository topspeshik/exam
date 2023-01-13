from threading import Thread


def printEven():
    for i in range(0, 11, 2):
        print(i)


def printOdd():
    for i in range(1, 11, 2):
        print(i)


thread1 = Thread(target=printEven())
thread2 = Thread(target=printOdd())
thread1.start()
thread2.start()
