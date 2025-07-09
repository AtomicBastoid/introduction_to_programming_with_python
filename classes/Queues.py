myQueue = ["" for _ in range(10)]
startptr = 0
rearptr = 0

def enqueue(item):
    global myQueue, startptr, rearptr
    if rearptr >= 10:
        print("Queue is full")
        return
    myQueue[rearptr] = item
    rearptr = rearptr + 1

def dequeue():
    global myQueue, startptr, rearptr
    if myQueue[startptr] == "":
        print("Queue is Empty")
        return 
    print(myQueue[startptr])
    myQueue[startptr] = ""
    startptr = startptr + 1

def peek():
    global myQueue, startptr, rearptr
    print(myQueue[startptr])

enqueue("p")
enqueue("y")
enqueue("t")
enqueue("h")
enqueue("o")
enqueue("n")
print(myQueue)

dequeue()
dequeue()
print(myQueue)
print(startptr)
